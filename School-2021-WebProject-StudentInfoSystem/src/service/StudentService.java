package service;

import bean.Student;

import java.rmi.StubNotFoundException;
import java.util.List;

public interface StudentService {
    /**
     * 获取所有学生的信息
     * @param name
     * @param stuno
     * @param sex
     * @param pageIndex 页面值
     * @param pageSize 每页显示的条目数
     * @return  包含学生信息的列表
     */
    public List<Student> getStudents(String name,String stuno,int sex,
                                     int pageIndex,int pageSize);

    /**
     * 获取查询结果的总条目数 (用于将结果分页显示)
     * @param name
     * @param stuno
     * @param sex
     * @return
     */
    public int total(String name,String stuno,int sex);

    /**
     * 新增学生
     * @param student
     * @return
     */
    public int insertStudent(Student student);

    /**
     * 主键查询学生信息
     * @param sid
     * @return
     */
    public Student findById (int sid);

    /**
     * 修改学生信息
     * @param student
     * @return
     */
    public int updateStudent(Student student);

    /**
     * 删除学生信息
     * @param student
     * @return
     */
    public int deleteStudent(String sid);

}
