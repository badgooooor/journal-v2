---
title: "Two AI tools worth trying: GSD and RTK"
description: "Quick thoughts on Get-Shit-Done and RTK — tools that improve AI coding workflows through better prompting structure and token optimization."
published: 2026/04/07
slug: "ai-tools"
tags:
  - ai
  - tools
  - coding
  - productivity
---

ช่วงนี้ได้ลองเครื่องที่ช่วยให้ coding agent ที่ใช้ประจำอย่าง Claude เลยอยากเอามาแชร์ประสบการณ์การใช้งานสั้นๆกัน

### Get-Shit-Done กับ metaprompting

ปัญหานึงที่เจอในงาน coding ปกติคือเรื่อง attention span ของ AI พอ context ใหญ่มากขึ้นเรื่อยๆ agent ก็เริ่มทำงานได้แย่ลงและให้ผลลัพธ์ที่ไม่ถูกต้อง มันก็มีหลายเทคนิคที่ช่วยได้ เช่น few-shot prompting แต่อีกอย่างที่หลายคนนิยมทำคือการกำหนด skills หรือ persona ตอนเริ่มต้น ซึ่งมาจากแนวคิดที่เรียกว่า "metaprompting"

Metaprompting คือเทคนิคการสร้าง prompt ที่เน้นไปที่ลักษณะของปัญหาและงานที่ต้องทำ เรียกได้ว่าเป็น "abstraction" ในแบบของ prompt engineering ลองดูใน prompt ของ tools ที่ใช้แนวคิดนี้อย่าง speckit จะเจอ pattern พวกนี้

1. มี format/pattern ของปัญหาและวิธีแก้
2. มี syntax ของ response/solution ที่คาดหวัง
3. มีตัวอย่างแบบ abstracted เพื่อแสดงโครงสร้างของปัญหาและวิธีแก้
4. ดึงแนวคิดจาก type theory มาจัดหมวดหมู่และจัดระเบียบตรรกะ

ฟังดูคล้าย AI memory แต่ generalized เนอะ?

นี่คือสิ่งที่ "Get-Shit-Done" ทำ มันมีชุด prompts สำหรับกำหนด requirements, วางแผน, research และ execute งานต่างๆ ผู้ใช้แค่ต้องมีเป้าหมายที่ชัดเจน จริงๆ แค่ประโยคเดียวก็พอ มันจะหา details ของ requirements เองแล้วถามกลับมา ซึ่งช่วยแก้ปัญหา "ไม่รู้ว่าตัวเองจะทำอะไรกันแน่" ได้ด้วย

![[[GSD usage](https://images.yuttakhanb.dev/Screenshot%202569-04-04%20at%2012.44.33.png)]]

จากที่ใช้มาหลายวัน พบว่ามันสอดคล้องกับสิ่งที่ developers หลายคนทำ (หรืออย่างน้อยก็ที่ผมทำ?) ผมชอบ research และวางแผนเยอะๆ ก่อน implement GSD ก็เลียนแบบสิ่งที่ผมทำได้ดี แถมยังช่วยในการตัดสินใจบน options ต่างๆ ได้ด้วย หรือถ้าอยากให้ AI ตัดสินใจให้หมดเลยก็ได้เหมือนกัน

### ประหยัด tokens ด้วย RTK

เนื่องจากงาน coding กิน tokens เยอะมาก การมี tools ช่วย optimize การใช้ tokens จึงเป็นเรื่องดี RTK ทำตัวเป็น CLI proxy ที่ตัด noises ออก (comments, whitespace, boilerplate) จัดกลุ่มรายการที่คล้ายกัน ตัด context ที่ไม่จำเป็น และ collapse log lines ที่ซ้ำกัน RTK รองรับโปรแกรมต่างๆ ที่ AI มักใช้ เช่น Git, test runners, compilers

```
  Without rtk:                                    With rtk:

  Claude  --git status-->  shell  -->  git         Claude  --git status-->  RTK  -->  git
    ^                                   |            ^                      |          |
    |        ~2,000 tokens (raw)        |            |   ~200 tokens        | filter   |
    +-----------------------------------+            +------- (filtered) ---+----------+
```

เท่าที่ลอง มันก็พอช่วยลด tokens ที่เกิดจาก CLI calls ได้ระดับนึง อาจจะมากบ้างน่้อยบ้างขึ้นอยู่กับ CLI ทำให้พอยืดระยะเวลาที่ใช้ LLM ก่อนที่จะติด limit ได้นิดนึง RTK ยังมีคำสั่งสำหรับดู analytics ของ tokens ที่ประหยัดไปได้ด้วย

### Conclusion

จากทั้ง 2 tools ที่ลองมา คิดว่ามันช่วยให้ใช้ AI เป็น assistant ได้ดีขึ้นอีกระดับนึง ถ้าสนใจใช้ ก็สามารถลองติดตั้งตาม guideline ใน Github repository ได้เลยครับ

GSD: https://github.com/gsd-build/get-shit-done
RTK: https://github.com/rtk-ai/rtk

ขอบคุณที่อ่านนะครับ
