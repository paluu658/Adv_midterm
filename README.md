# Resale Flat Management System

A Django-based application to manage and explore HDB resale flats. This application provides both API endpoints and a user-friendly web interface for managing data related to resale flats.

## **Features**

- **View All Flats**: List all flats in the database.
- **Filter Flats by Town**: Filter flats based on the town name.
- **Filter Flats by Price Range**: View flats within a specific price range.
- **Group Flats by Type**: See how many flats exist for each flat type.
- **Average Price by Town**: Check the average resale price for flats in each town.
- **Add New Flat**: Create a new flat entry via a web form or API.

---

## **Prerequisites**

1. Python 3.8 or later
2. pip (Python package installer)
3. Virtual environment tool (optional but recommended)

---

## **Setup Instructions**

### **1. Clone the Repository**

```bash
git clone <repository-url>
cd <repository-folder>
```

### **2. Create a Virtual Environment (Optional)**

```bash
python -m venv venv
source venv/bin/activate
```

### **3. Install Required Packages**

```bash
pip install -r requirements.txt
```

### **4. Run Migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

### **5. Data Setup**

```bash
python scripts/load_and_store.py
```

### **6. Run the Application**

```bash
python manage.py runserver
```

### **7. Access the Application**

Open a web browser and go to `http://127.0.0.1:8000/` to access the application.

---

## **Testing**

To run the tests, execute the following command:

```bash
python manage.py test
```

---
