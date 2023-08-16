package service.impl;

import bean.Student;
import dao.StudentDao;
import dao.impl.StudentDaoImpl;
import service.StudentService;

import java.util.List;

public class StudentServiceImpl implements StudentService {
    private StudentDao studentDao = new StudentDaoImpl();

    @Override
    public List<Student> getStudents(String name,String stuno,int sex,int pageIndex,int pageSize) {
        return studentDao.getStudents(name, stuno, sex,pageIndex,pageSize);
    }

    @Override
    public int total(String name, String stuno, int sex) {
        return studentDao.total(name, stuno, sex);
    }

    @Override
    public int insertStudent(Student student) {
        return studentDao.insertStudent(student);
    }

    @Override
    public Student findById(int sid) {
        return studentDao.findById(sid);
    }

    @Override
    public int updateStudent(Student student) {
        return studentDao.updateStudent(student);
    }

    @Override
    public int deleteStudent(String sid) {
        return studentDao.deleteStudent(sid);
    }
}
