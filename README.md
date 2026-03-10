# Student Management System

## 🎯 Mục tiêu
Xây dựng hệ thống quản lý sinh viên với đầy đủ chức năng CRUD và mở rộng.

## 👨‍💻 Thông tin cá nhân
- **Họ và tên**: Nguyễn Thị Phương Thảo
- **Lớp**: KHDL19B

## 🛠 Tech Stack
- **Frontend**: React 18 + Axios
- **Backend**: FastAPI + SQLAlchemy
- **Database**: SQLite
- **Development Tools**: Windsurf

## 📋 Công cụ và môi trường
- **IDE**: Windsurf
- **Language**: Python, JavaScript
- **Package Manager**: npm, pip
- **Version Control**: Git

## � Hướng dẫn cài đặt và chạy

### Backend Setup
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

### Frontend Setup
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

## � Tính năng

### Phase 1 - MVP
- ✅ Thêm sinh viên mới
- ✅ Xem danh sách sinh viên
- ✅ Chỉnh sửa thông tin sinh viên
- ✅ Xóa sinh viên

### Phase 2 - Mở rộng
- ✅ Quản lý lớp học (Class)
- ✅ Tìm kiếm sinh viên theo tên
- ✅ Thống kê dữ liệu
- ✅ Xuất dữ liệu CSV
- ✅ Import dữ liệu từ CSV

## 📁 Cấu trúc project
```
vibe_coding1/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── models.py            # Database models
│   ├── database.py          # Database setup
│   ├── requirements.txt     # Python dependencies
│   └── students.db          # SQLite database
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── StudentList.js    # Component danh sách
│   │   │   ├── StudentForm.js    # Component form
│   │   │   └── Statistics.js    # Component thống kê
│   │   ├── App.js           # Main app
│   │   ├── App.css          # Styles
│   │   ├── index.js         # Entry point
│   │   └── index.css        # Global styles
│   ├── public/
│   │   └── index.html       # HTML template
│   └── package.json         # Node.js dependencies
├── student.csv              # Student data file
├── class.csv                # Class data file
├── PLAN.md                  # Kế hoạch chi tiết
└── README.md                # This file
```

## � API Endpoints

### Students
- `GET /students` - Lấy danh sách sinh viên
- `POST /students` - Thêm sinh viên mới
- `PUT /students/{student_id}` - Cập nhật sinh viên
- `DELETE /students/{student_id}` - Xóa sinh viên
- `GET /students/search?name=` - Tìm kiếm sinh viên
- `POST /students/import` - Import sinh viên từ CSV

### Classes
- `GET /classes` - Lấy danh sách lớp
- `POST /classes` - Thêm lớp mới
- `PUT /classes/{class_id}` - Cập nhật lớp
- `DELETE /classes/{class_id}` - Xóa lớp
- `POST /classes/import` - Import lớp từ CSV

### Other
- `GET /statistics` - Lấy thống kê
- `GET /export/csv` - Xuất CSV

## 🎨 Giao diện
- **Responsive design**: Tương thích mobile và desktop
- **Modern UI**: Sử dụng CSS grid và flexbox
- **Interactive**: Real-time validation và feedback
- **Search**: Tìm kiếm instant
- **Statistics**: Dashboard với cards và charts

## 📝 Dữ liệu mẫu

### Students (student.csv)
```csv
student_id,name,birth_year,major,gpa
S001,Nguyen Van A,2002,Khoa học máy tính,3.5
S002,Le Thi B,2001,Khoa học máy tính,3.7
S003,Tran Van C,2002,Kỹ thuật phần mềm,3.4
```

### Classes (class.csv)
```csv
class_id,class_name,advisor
C01,Khoa học máy tính 1,Nguyen Van A
C02,Kỹ thuật phần mềm 1,Le Thi B
C03,Mạng máy tính 1,Tran Van C
```

## 🔄 Quá trình thực hiện

### Vibe Coding Process
1. **Prompt Engineering** → Viết prompt chi tiết
2. **AI Code Generation** → AI tạo code backend/frontend
3. **Code Review** → Kiểm tra và sửa lỗi
4. **Testing** → Test tất cả chức năng
5. **Refinement** → Cải thiện dựa trên feedback

### Log quá trình
- **Phase 1**: Xây dựng MVP cơ bản
- **Phase 2**: Mở rộng tính năng nâng cao
- **CORS Issues**: Giải quyết cross-origin problems
- **CSV Import/Export**: Implement data management

## 🎯 Kết quả
- ✅ **MVP hoàn thành**: CRUD functionality working
- ✅ **Phase 2 hoàn thành**: Advanced features implemented
- ✅ **Data Import**: CSV files auto-imported
- ✅ **Export Functionality**: CSV download working
- ✅ **Search**: Real-time search implemented
- ✅ **Statistics**: Dashboard with analytics
- ✅ **Responsive**: Mobile-friendly design

## 🚀 Triển khai
- **Development**: Local environment
- **Production**: Docker containerization
- **Testing**: Manual and automated testing
- **Documentation**: README và inline comments

---

**Status**: ✅ Hoàn thành - Sẵn sàng sử dụng!

**Last Updated**: 10/03/2026
**Version**: 2.0.0 Year, Major, GPA

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
