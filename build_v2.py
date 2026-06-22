import os

dir_path = "/Users/wattanapongtabthanee/.gemini/antigravity/scratch/thepsathit-ready2"

replacements = {
    # Text changes
    "Nakae Dole": "ThepSathit",
    "อำเภอนาแก": "อำเภอเทพสถิต",
    "nakae_": "thepsathit_",
    "NakaeStore": "ThepSathitStore",
    
    # Contact Link and Text (Before replacing Nakae Dole)
    # Wait, if "Nakae Dole" is replaced first, "ช่องทางติดต่อ Nakae Dole" becomes "ช่องทางติดต่อ ThepSathit".
    # Since I'm using a dict, order matters in Python > 3.7. Let's just do it directly.
    "ช่องทางติดต่อ Nakae Dole": "ติดต่อ สกร.",
    "https://line.me/R/ti/p/@869fjgcd": "https://www.facebook.com/people/ศูนย์ส่งเสริมการเรียนรู้ระดับอำเภอเทพสถิต-จังหวัดชัยภูมิ/100086008583880/",
    
    # URLs and passwords
    "https://script.google.com/macros/s/AKfycbwypQUXdZOZ1__Hjl9KZwH8L65Hp-PJE1Hu9a_hTneOhS8oXHbwNOK_cZJWNvU6zc56/exec": "https://script.google.com/macros/s/AKfycbyObT_BWxrhzF2LxIlggfeN6_SvIudT1unYlfCcT3IYJeTSga05IupWc9_OgZPYy2S4/exec",
    "https://img2.pic.in.th/.5767ec9fdaa5699b.png": "https://img2.pic.in.th/a986af70f1d95baee0e9c664522b45e8.png",
    'const ADMIN_PASSWORD = "admin0";': 'const ADMIN_PASSWORD = "0admin";',
    
    # Footer replacement
    "<p>ระบบ ศูนย์ส่งเสริมการเรียนรู้ระดับอำเภอนาแก</p>\n      <p>Nakae To Share</p>": "<p>ศูนย์ส่งเสริมการเรียนรู้ระดับอำเภอเทพสถิต</p>",
    
    # Theme colors (Indigo/Violet for a modern look)
    "--brand: #0f766e; /* Teal */": "--brand: #4f46e5; /* Modern Indigo */",
    "--brand-deep: #115e59;": "--brand-deep: #312e81;",
    "--brand-light: #14b8a6;": "--brand-light: #818cf8;"
}

# Fix footer order issue with "อำเภอนาแก" already replaced
# Wait, "อำเภอนาแก" is replaced, so the footer string will actually be "<p>ระบบ ศูนย์ส่งเสริมการเรียนรู้ระดับอำเภอเทพสถิต</p>\n      <p>ThepSathit To Share</p>"
# Let's adjust replacements dict to be safe:

ordered_replacements = [
    ("ช่องทางติดต่อ Nakae Dole", "ติดต่อ สกร."),
    ("https://line.me/R/ti/p/@869fjgcd", "https://www.facebook.com/people/ศูนย์ส่งเสริมการเรียนรู้ระดับอำเภอเทพสถิต-จังหวัดชัยภูมิ/100086008583880/"),
    ("<p>ระบบ ศูนย์ส่งเสริมการเรียนรู้ระดับอำเภอนาแก</p>\n      <p>Nakae To Share</p>", "<p>ศูนย์ส่งเสริมการเรียนรู้ระดับอำเภอเทพสถิต</p>"),
    ("Nakae Dole", "ThepSathit"),
    ("อำเภอนาแก", "อำเภอเทพสถิต"),
    ("nakae_", "thepsathit_"),
    ("NakaeStore", "ThepSathitStore"),
    ("https://script.google.com/macros/s/AKfycbwypQUXdZOZ1__Hjl9KZwH8L65Hp-PJE1Hu9a_hTneOhS8oXHbwNOK_cZJWNvU6zc56/exec", "https://script.google.com/macros/s/AKfycbyObT_BWxrhzF2LxIlggfeN6_SvIudT1unYlfCcT3IYJeTSga05IupWc9_OgZPYy2S4/exec"),
    ("https://img2.pic.in.th/.5767ec9fdaa5699b.png", "https://img2.pic.in.th/a986af70f1d95baee0e9c664522b45e8.png"),
    ('const ADMIN_PASSWORD = "admin0";', 'const ADMIN_PASSWORD = "0admin";'),
    ("--brand: #0f766e; /* Teal */", "--brand: #4f46e5; /* Modern Indigo */"),
    ("--brand-deep: #115e59;", "--brand-deep: #312e81;"),
    ("--brand-light: #14b8a6;", "--brand-light: #818cf8;")
]

for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith((".html", ".js", ".css")):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            for old, new in ordered_replacements:
                content = content.replace(old, new)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

# Now create the artifact
out_path = "/Users/wattanapongtabthanee/.gemini/antigravity/brain/acae60da-9801-4132-87ae-8ac52cfcc9fd/ThepSathit_V2.md"
files_to_include = [
    "index.html",
    "admin/index.html",
    "assets/styles.css",
    "assets/app.js",
    "assets/admin.js"
]

content = "# อัปเดตไฟล์ ThepSathit E-Learning (เวอร์ชัน 2)\n\nผมได้ปรับแก้ตามที่คุณขอเรียบร้อยแล้วครับ ทั้งโลโก้, เมนูติดต่อ, รหัสผ่าน, และเปลี่ยนโทนสีเป็น **Modern Indigo (สีม่วงคราม)** ซึ่งเป็นสียอดนิยมของวงการ Tech Education และดูทันสมัยมากครับ!\n\n"
content += "รบกวนก๊อปปี้ไฟล์ทั้ง 5 ด้านล่างนี้ไปวางทับไฟล์เดิมใน GitHub ได้เลยครับ:\n\n"

for rel_path in files_to_include:
    full_path = os.path.join(dir_path, rel_path)
    ext = rel_path.split('.')[-1]
    lang = ext if ext != "js" else "javascript"
    
    with open(full_path, "r", encoding="utf-8") as f:
        file_data = f.read()
        
    content += f"### ไฟล์: `{rel_path}`\n\n"
    content += f"```{lang}\n{file_data}\n```\n\n"

with open(out_path, "w", encoding="utf-8") as f:
    f.write(content)

