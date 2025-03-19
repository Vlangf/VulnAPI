from fastapi import Form, APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/contact", response_class=HTMLResponse)
def contact_form():
    """
    Shows the contact form with a CAPTCHA
    """
    form = f"""
        <form action="/contact" method="post">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message" required></textarea>
            <img src="captcha.jpg" alt="CAPTCHA">
            <input type="text" name="captcha" placeholder="Enter the code above" required>
            <input type="submit" value="Send">
        </form>
    """
    return form


@router.post("/contact")
def send_message(name: str = Form(...), email: str = Form(...), message: str = Form(...),
                 captcha: str = Form(...)):
    """
    Sends a message after verifying the CAPTCHA
    """
    if captcha == "1234":
        return {"result": "Message sent successfully"}
    else:
        return {"error": "Invalid CAPTCHA"}
