# 🛒 Django eCommerce Project

An eCommerce web application built with Django, offering a modern online shopping experience including product listings, cart management, user authentication, and order tracking.

## 🚀 Features

- User Registration and Login
- Product Listings with Categories
- Product Search and Filtering
- Shopping Cart and Checkout
- Order History and Invoice Generation
- Admin Dashboard for Product and Order Management
- Responsive UI (Bootstrap/Tailwind)

## 📁 Project Structure
![struc](https://github.com/user-attachments/assets/e82ccaf3-7a49-4e41-b7f2-d2a43f7bb7b4)

## 🛠️ Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/DudulBiswal/Ecommmerce.git
   cd Ecommmerce
   
2. **Create a Virtual Environment**
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   
4. **Install Dependencies**
   pip install -r requirements.txt
   
5. **Run Migrations**
  python manage.py migrate

6. **Create a Superuser**
   python manage.py createsuperuser

7. **Run the Development Server**
   python manage.py runserver

8. **Access the Application**
   Frontend: http://localhost:8000
   Admin Panel: http://localhost:8000/admin

🔐 Environment Variables
Create a .env file in the root directory for secrets and configurations:

ini
Copy
Edit
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
🧪 Running Tests
bash
Copy
Edit
python manage.py test
📦 Dependencies
Django

Pillow (for image uploads)

django-crispy-forms or similar (for better form styling)

Stripe / PayPal SDKs (if payment integration is included)

📸 Screenshots
(Add screenshots of homepage, product page, cart, admin panel here)

👨‍💻 Contributors
Your Name

Contributor 2

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

python
Copy
Edit

Let me know if you'd like to include specific technologies (like DRF, React frontend, etc.) or tailor it to a real project you're working on!









