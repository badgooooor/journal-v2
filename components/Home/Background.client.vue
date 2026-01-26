<template>
  <div
    class="pointer-events-none absolute left-0 top-0 h-full w-full"
    style="z-index: 0"
  >
    <div ref="mountRef" class="h-full w-full"></div>
    <div
      class="absolute left-0 top-0 h-full w-full backdrop-blur-sm"
      style="z-index: 1"
    ></div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from "vue";
import * as THREE from "three";

const mountRef = ref<HTMLDivElement | null>(null);
let animationId: number | null = null;
let renderer: THREE.WebGLRenderer | null = null;
let geometry: THREE.PlaneGeometry | null = null;
let material: THREE.ShaderMaterial | null = null;
let resizeHandler: (() => void) | null = null;

onMounted(() => {
  if (!mountRef.value) return;

  // Get the parent container's dimensions
  const parent = mountRef.value.parentElement;
  if (!parent) return;

  const updateSize = () => {
    const rect = parent.getBoundingClientRect();
    return { width: rect.width, height: rect.height };
  };

  let { width, height } = updateSize();

  // Scene setup
  const scene = new THREE.Scene();

  // Camera setup - using orthographic camera for full-screen effect
  const camera = new THREE.OrthographicCamera(-1, 1, 1, -1, 0.1, 1000);
  camera.position.z = 1;

  // Renderer setup
  renderer = new THREE.WebGLRenderer({
    antialias: true,
    alpha: true,
    preserveDrawingBuffer: false,
  });
  renderer.setSize(width, height);
  renderer.setClearColor(0x000000, 0);
  renderer.setPixelRatio(window.devicePixelRatio);

  // Custom vertex shader
  const vertexShader = `
    varying vec2 vUv;

    void main() {
      vUv = uv;
      gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
    }
  `;

  // Shadertoy: https://www.shadertoy.com/view/tdG3Rd
  const fragmentShader = `
    #ifdef GL_ES
      precision lowp float;
    #endif

    uniform float u_time;
    uniform vec2 u_resolution;

    varying vec2 vUv;

    float colormap_red(float x) {
      if (x < 0.0) {
        return 54.0 / 255.0;
      } else if (x < 20049.0 / 82979.0) {
        return (829.79 * x + 54.51) / 255.0;
      } else {
        return 1.0;
      }
    }

    float colormap_green(float x) {
      if (x < 20049.0 / 82979.0) {
        return 0.0;
      } else if (x < 327013.0 / 810990.0) {
        return (8546482679670.0 / 10875673217.0 * x - 2064961390770.0 / 10875673217.0) / 255.0;
      } else if (x <= 1.0) {
        return (103806720.0 / 483977.0 * x + 19607415.0 / 483977.0) / 255.0;
      } else {
        return 1.0;
      }
    }

    float colormap_blue(float x) {
      if (x < 0.0) {
        return 54.0 / 255.0;
      } else if (x < 7249.0 / 82979.0) {
        return (829.79 * x + 54.51) / 255.0;
      } else if (x < 20049.0 / 82979.0) {
        return 127.0 / 255.0;
      } else if (x < 327013.0 / 810990.0) {
        return (792.02249341361393720147485376583 * x - 64.364790735602331034989206222672) / 255.0;
      } else {
        return 1.0;
      }
    }

    vec4 colormap(float x) {
      return vec4(colormap_red(x), colormap_green(x), colormap_blue(x), 1.0);
    }

    float rand(vec2 n) {
      return fract(sin(dot(n, vec2(12.9898, 4.1414))) * 43758.5453);
    }

    float noise(vec2 p) {
      vec2 ip = floor(p);
      vec2 u = fract(p);
      u = u * u * (3.0 - 2.0 * u);

      float res = mix(
        mix(rand(ip), rand(ip + vec2(1.0, 0.0)), u.x),
        mix(rand(ip + vec2(0.0, 1.0)), rand(ip + vec2(1.0, 1.0)), u.x),
        u.y
      );
      return res * res;
    }

    const mat2 mtx = mat2(0.80, 0.60, -0.60, 0.80);

    float fbm(vec2 p) {
      float f = 0.0;

      f += 0.800000 * noise(p + u_time);
      p = mtx * p * 2.02;
      f += 0.051250 * noise(p);
      p = mtx * p * 2.01;
      f += 0.250000 * noise(p);
      p = mtx * p * 2.03;
      f += 0.125000 * noise(p);
      p = mtx * p * 2.01;
      f += 0.062500 * noise(p);
      p = mtx * p * 2.04;
      f += 0.015625 * noise(p + sin(u_time));

      return f / 0.96875;
    }

    float pattern(in vec2 p) {
      return fbm(p + fbm(p + fbm(p)));
    }

    void main() {
      // Use vUv for proper UV coordinates
      vec2 uv = vUv;
      float shade = pattern(uv * 3.0); // Scale the pattern

      // Output final color with reduced opacity for background effect
      gl_FragColor = vec4(colormap(shade).rgb, 0.3);
    }
  `;

  // Create plane geometry that covers the full screen
  geometry = new THREE.PlaneGeometry(2, 2);

  // Create shader material
  material = new THREE.ShaderMaterial({
    vertexShader,
    fragmentShader,
    uniforms: {
      u_time: { value: 0.0 },
      u_resolution: { value: new THREE.Vector2(width, height) },
    },
    transparent: true,
    side: THREE.DoubleSide,
  });

  // Create mesh
  const mesh = new THREE.Mesh(geometry, material);
  scene.add(mesh);

  // Mount the renderer
  renderer.domElement.style.display = "block";
  renderer.domElement.style.width = "100%";
  renderer.domElement.style.height = "100%";
  mountRef.value.appendChild(renderer.domElement);

  // Handle resize
  resizeHandler = () => {
    const newSize = updateSize();
    width = newSize.width;
    height = newSize.height;

    if (renderer && material) {
      renderer.setSize(width, height);
      material.uniforms.u_resolution.value.set(width, height);
    }
  };

  window.addEventListener("resize", resizeHandler);

  // Animation loop
  const animate = (time: number) => {
    animationId = requestAnimationFrame(animate);

    // Update time uniform
    if (material) {
      material.uniforms.u_time.value = time * 0.001;
    }

    if (renderer) {
      renderer.render(scene, camera);
    }
  };

  animate(0);
});

onUnmounted(() => {
  // Cancel animation frame
  if (animationId !== null) {
    cancelAnimationFrame(animationId);
  }

  // Remove resize event listener
  if (resizeHandler) {
    window.removeEventListener("resize", resizeHandler);
  }

  // Remove renderer from DOM
  if (mountRef.value && renderer?.domElement) {
    mountRef.value.removeChild(renderer.domElement);
  }

  // Dispose of resources
  if (geometry) geometry.dispose();
  if (material) material.dispose();
  if (renderer) renderer.dispose();
});
</script>
