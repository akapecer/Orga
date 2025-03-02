# **Orga - Cyclical Menu Management**  

**Orga** is a web application designed to efficiently manage cyclical menus for businesses, restaurants, and institutions. Built with **Django** for the backend and **PostgreSQL** as the database, Orga allows administrators to create and manage dishes, assign allergens, and generate dynamic menus with historical tracking.  

## **Features**  
- 📌 **Dish Management**: Add, edit, and categorize dishes with allergen tracking.  
- 📅 **Cyclical Menu Creation**: Build menus using registered dishes and maintain a history of past menus.  
- 📜 **PDF Export**: Generate and download the latest menu as a PDF.  
- 🔐 **Role-based Access**:  
  - **Superuser**: Full control over the system.  
  - **User**: Can only view and download the latest menu.  
- 💾 **Database Integration**: Uses **PostgreSQL** for reliable data storage.  
- 🚀 **API-First Architecture**: Designed for seamless integration with external applications.  

## **Tech Stack**  
- **Backend**: Django  
- **Database**: PostgreSQL  
- **Authentication**: Email & Password-based login  
- **Deployment**: _(To be determined)_  

## **Installation**  
1. Clone the repository:  
   ```sh  
   git clone https://github.com/your-username/orga.git  
   ```  
2. Navigate to the project directory:  
   ```sh  
   cd orga/backend  
   ```  
3. Create a virtual environment and activate it:  
   ```sh  
   python -m venv venv  
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`  
   ```  
4. Install dependencies:  
   ```sh  
   pip install -r requirements.txt  
   ```  
5. Run migrations:  
   ```sh  
   python manage.py migrate  
   ```  
6. Start the development server:  
   ```sh  
   python manage.py runserver  
   ```  

## **Usage**  
- Access the admin panel at `http://127.0.0.1:8000/admin/`  
- Create and manage dishes, categories, and allergens.  
- Generate and export menus as PDFs.  

## **Contributing**  
Contributions are welcome! Feel free to fork the repository and submit a pull request.  

## **License**  
This project is licensed under the MIT License.  

## **Contact**  
For any inquiries, please contact [your-email@example.com](mailto:your-email@example.com).  

