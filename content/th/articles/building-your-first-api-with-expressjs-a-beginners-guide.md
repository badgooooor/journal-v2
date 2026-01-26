---
title: "สร้าง API แรกของคุณด้วย Express.js: คู่มือสำหรับผู้เริ่มต้น"
description: "คู่มือที่เข้าใจง่ายสำหรับการสร้าง API แรกของคุณด้วย Express.js"
published: 2023/11/2
slug: "building-your-first-api-with-expressjs-a-beginners-guide"
---

> บทความนี้สร้างขึ้นโดยใช้ ChatGPT และมีไว้เป็นตัวอย่างเท่านั้น

## Express.js คืออะไร?

Express.js เป็น Node.js web application framework ที่มีขนาดเล็กและยืดหยุ่น ซึ่งมีคุณสมบัติที่แข็งแกร่งในการพัฒนาเว็บและมอบายแอปพลิเคชัน มันช่วยให้การพัฒนาเว็บแอปพลิเคชันที่ใช้ Node เป็นไปอย่างรวดเร็ว และถูกนำมาใช้อย่างแพร่หลายในการสร้าง API เนื่องจากความเรียบง่ายและประสิทธิภาพ

## ขั้นตอนที่ 1: ตั้งค่าสภาพแวดล้อมของคุณ

ก่อนที่คุณจะเริ่มต้น ตรวจสอบให้แน่ใจว่าคุณได้ติดตั้ง Node.js บนระบบของคุณแล้ว คุณสามารถดาวน์โหลดได้จากเว็บไซต์อย่างเป็นทางการของ Node.js

เมื่อติดตั้ง Node.js แล้ว คุณสามารถเริ่มต้นโปรเจกต์ของคุณได้:

```bash
mkdir my-express-api
cd my-express-api
npm init -y
```

คำสั่งนี้จะสร้างไดเรกทอรีใหม่สำหรับโปรเจกต์ของคุณและเริ่มต้นโปรเจกต์ Node.js ใหม่

## ขั้นตอนที่ 2: ติดตั้ง Express.js

ติดตั้ง Express.js โดยใช้ npm (Node Package Manager):

```bash
npm install express --save
```

คำสั่งนี้จะติดตั้ง Express.js และเพิ่มลงใน dependencies ของโปรเจกต์

## ขั้นตอนที่ 3: สร้าง Express Server แรกของคุณ

สร้างไฟล์ชื่อ app.js ในไดเรกทอรีโปรเจกต์ของคุณ ไฟล์นี้จะเป็นจุดเริ่มต้นของ API ของคุณ เพิ่มโค้ดต่อไปนี้ลงใน app.js:

```js
const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});
```

โค้ดนี้จะสร้าง Express server พื้นฐานที่รับฟังที่พอร์ต 3000 และตอบกลับด้วย "Hello World!" สำหรับ HTTP GET requests ที่ไปยัง root URL (/)

## ขั้นตอนที่ 4: รัน Express Server ของคุณ

รันเซิร์ฟเวอร์ของคุณโดยใช้ Node.js:

```bash
node app.js
```

เข้าชม http://localhost:3000 ในเบราว์เซอร์ของคุณ คุณควรจะเห็นข้อความ "Hello World!"

## ขั้นตอนที่ 5: สร้าง API แบบง่าย

ตอนนี้มาขยายเซิร์ฟเวอร์ของเราให้ทำงานเป็น API แบบง่าย ๆ กันเถอะ ตัวอย่างเช่น มาสร้าง endpoint ที่ส่งคืนรายชื่อผู้ใช้

เพิ่มโค้ดต่อไปนี้ลงใน app.js ของคุณ:

```javascript
let users = [{ name: "Alice" }, { name: "Bob" }];

app.get('/users', (req, res) => {
  res.json(users);
});
```

ตอนนี้ ถ้าคุณเข้าชม http://localhost:3000/users คุณจะเห็น JSON representation ของ users array

## ขั้นตอนที่ 6: ทดสอบ API ของคุณ

การทดสอบ API ของคุณเป็นสิ่งสำคัญ คุณสามารถใช้เครื่องมือเช่น Postman หรือ curl เพื่อทดสอบ endpoints ของคุณ

## ขั้นตอนที่ 7: ขั้นตอนต่อไป

จากจุดนี้ คุณสามารถเริ่มสร้าง API ที่ซับซ้อนมากขึ้น พิจารณาสิ่งต่อไปนี้:

- การใช้งาน CRUD (Create, Read, Update, Delete) operations
- เชื่อมต่อ API ของคุณกับฐานข้อมูล
- เพิ่ม authentication และ authorization
- จัดระเบียบโค้ดของคุณด้วย routers และ controllers

## บทสรุป

Express.js ทำให้กระบวนการสร้าง API ใน Node.js ง่ายขึ้น เป็นจุดเริ่มต้นที่ดีสำหรับนักพัฒนาที่ต้องการเจาะลึกในการพัฒนา backend ด้วยแนวทางที่เรียบง่าย คุณมีอิสระในการจัดโครงสร้างแอปพลิเคชันของคุณตามที่คุณเห็นสมควร ทำให้ Express.js เป็นเครื่องมือที่มีค่าอย่างยิ่งในชุดเครื่องมือการพัฒนาของคุณ
