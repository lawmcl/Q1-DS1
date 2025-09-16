from js import document

def compute_area(event=None):   # accept event so PyScript can call it
    try:
        b1 = float(document.getElementById("base1").value)
        b2 = float(document.getElementById("base2").value)
        h = float(document.getElementById("height").value)
        area = 0.5 * (b1 + b2) * h
        document.getElementById("output").innerText = f"Area = {area}"
    except Exception:
        document.getElementById("output").innerText = "Please enter valid numbers."
