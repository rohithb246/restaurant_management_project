from utils.email utils import send_order_confirmation_email

result = send_order_confirmation_email(
    order_id=1234,
    customer_email="customer@example.com",
    customer_name="rohith",
    order_summary_html="<p>Item A x1 - 100</p><p>Total: 100 </p>",
    order_summary_text="Item A x1 = 100\n Total:100"
    
)

if not result['success']:
    print("Email Failed:", result["message"], result.get("error"))