# 🐶 Dog Shopping Site (Flask App)
A simple, scalable, and modular Flask web application for browsing and managing dog-related products. Built using Flask Blueprints, this project cleanly separates admin and user functionality, making it easy to maintain and extend.

## 🌟 Features
🛍️ User/Public
- View all available dog-related products
- Search products by name or category
- View product details (price, description, etc.)
- User registration and login

### 🔐 Admin Panel
---
- Add new products
- Edit existing product details
- Delete products from inventory
- Admin-level search functionality
- Secured admin access

### ⚙️ Development Architecture
---
- Modular Blueprints for user and admin sections
- Easy to scale and maintain

### 🛠 Tech Stack
---
- Layer	Technology
- Backend	Python, Flask
- Database	SQLite (can be upgraded to PostgreSQL or MySQL)
- Frontend	HTML, Bootstrap (optional)
- ORM	SQLAlchemy
- Authentication	Flask-Login

### 🔐 Admin Access
---
- Admin routes are protected using Flask-Login.
- Ensure admin credentials are set up in the database manually or via an admin registration route (optional setup script recommended).

### 🧪 Future Improvements
---
- Product image upload support
- Category filtering
- Shopping cart and checkout system
- Admin dashboard with analytics
