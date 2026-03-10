# Student Management System - Phase 1 MVP

## 🎯 Mục tiêu
Xây dựng hệ thống quản lý sinh viên đơn giản với đầy đủ chức năng CRUD.

## ✨ Chức năng (Phase 1 - MVP)
- ✅ Thêm sinh viên mới
- ✅ Xem danh sách sinh viên
- ✅ Chỉnh sửa thông tin sinh viên
- ✅ Xóa sinh viên

## 📊 Thông tin sinh viên
- **student_id**: Mã sinh viên (string)
- **name**: Họ tên (string)
- **birth_year**: Năm sinh (integer)
- **major**: Ngành học (string)
- **gpa**: Điểm trung bình (float)

## 🛠 Tech Stack
- **Frontend**: React 18 + Axios
- **Backend**: FastAPI + SQLAlchemy
- **Database**: SQLite

## 📁 Cấu trúc project
```
vibe_coding1/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── models.py            # Database models
│   ├── database.py          # Database setup
│   └── requirements.txt     # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── StudentList.js    # Component danh sách
│   │   │   └── StudentForm.js    # Component form
│   │   ├── App.js           # Main app
│   │   ├── App.css          # Styles
│   │   ├── index.js         # Entry point
│   │   └── index.css        # Global styles
│   ├── public/
│   │   └── index.html       # HTML template
│   └── package.json         # Node.js dependencies
├── PLAN.md                  # Kế hoạch chi tiết
└── README.md                # This file
```

## 🚀 Hướng dẫn cài đặt và chạy

### Backend
1. Mở terminal, vào thư mục backend:
   ```bash
   cd D:\vibe_coding1\backend
   ```

2. Tạo virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Cài đặt dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Chạy FastAPI server:
   ```bash
   python main.py
   ```

Backend sẽ chạy tại `http://localhost:8000`

### Frontend
1. Mở terminal khác, vào thư mục frontend:
   ```bash
   cd D:\vibe_coding1\frontend
   ```

2. Cài đặt dependencies:
   ```bash
   npm install
   ```

3. Chạy React development server:
   ```bash
   npm start
   ```

Frontend sẽ chạy tại `http://localhost:3000`

## 📡 API Endpoints

### Students
- `GET /students` - Lấy danh sách tất cả sinh viên
- `POST /students` - Thêm sinh viên mới
- `PUT /students/{student_id}` - Cập nhật thông tin sinh viên
- `DELETE /students/{student_id}` - Xóa sinh viên

### Root
- `GET /` - Thông tin API

## 🎨 Giao diện
- **Màn hình chính**: Form thêm/sửa sinh viên + Bảng danh sách sinh viên
- **Bảng sinh viên**: Hiển thị ID, Name, Major, GPA, Action (Edit/Delete)
- **Form**: Các trường Student ID, Name, Birth Year, Major, GPA

## ✅ Testing
1. Khởi động cả backend và frontend
2. Mở browser tại `http://localhost:3000`
3. Test các chức năng:
   - Thêm sinh viên mới
   - Xem danh sách sinh viên
   - Chỉnh sửa thông tin sinh viên
   - Xóa sinh viên

## 🔄 Phase 2 (Sắp tới)
- Thêm quản lý lớp học (Class)
- Tìm kiếm sinh viên theo tên
- Thống kê dữ liệu
- Export CSV

---

**Status**: ✅ Phase 1 MVP Hoàn thành
