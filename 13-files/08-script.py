js_code = """
console.log("Hello from JS script generated from Python");
const sum = (a, b) => a + b;
"""


with open("script.js", "w") as file:
  file.write(js_code)