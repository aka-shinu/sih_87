@echo off
echo 🚀 Mental Health Platform - Quick Start
echo =====================================

echo.
echo 📋 Setting up Backend...
cd backend

echo.
echo 🔧 Creating virtual environment...
python -m venv venv

echo.
echo 🔌 Activating virtual environment...
call venv\Scripts\activate

echo.
echo 📦 Installing backend dependencies...
pip install -r requirements.txt
pip install -r mental_health_platform\ai\requirements.txt

echo.
echo 🗄️ Setting up database...
python manage.py makemigrations
python manage.py migrate

echo.
echo 👤 Creating superuser (optional)...
echo Press Ctrl+C to skip superuser creation
python manage.py createsuperuser

echo.
echo 📁 Collecting static files...
python manage.py collectstatic --noinput

echo.
echo 🎨 Setting up Frontend...
cd ..\frontend

echo.
echo 📦 Installing frontend dependencies...
npm install

echo.
echo 🏗️ Building frontend...
npm run build

echo.
echo 🧠 Testing AI models...
cd ..\backend
python test_ai.py

echo.
echo ✅ Setup Complete!
echo.
echo 🚀 Starting servers...
echo.
echo Backend: http://localhost:8000
echo Frontend: http://localhost:3000
echo AI Test: http://localhost:8000/ai-test/
echo Admin: http://localhost:8000/admin/
echo.
echo Press any key to start the backend server...
pause

echo.
echo 🔥 Starting Django server...
python manage.py runserver

pause

