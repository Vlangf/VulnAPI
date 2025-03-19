from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/transfer")
def _transfer_money(to: str, amount: float):
    """
    Transfers the specified amount to the specified account
    """
    return {"result": f"Transferred {amount} to {to} successfully"}


@router.get("/transfer_form", response_class=HTMLResponse)
def transfer_form():
    """
    Displays a form for transferring money
    """
    form = f"""
        <form action="/transfer" method="post">
            <input type="hidden" name="to" value="attacker_account">
            <label for="amount">Amount:</label>
            <input type="number" name="amount" id="amount" value="1000">
            <input type="submit" value="Transfer">
        </form>
    """
    return form
