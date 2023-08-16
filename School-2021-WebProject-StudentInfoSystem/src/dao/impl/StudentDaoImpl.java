package dao.impl;

import bean.Student;
import dao.StudentDao;
import util.DBUtils;
import util.StudentEnum;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class StudentDaoImpl extends DBUtils implements StudentDao {
    @Override
    public List<Student> getStudents(String name, String stuno, int sex, int pageIndex, int pageSize) {

        List list = new ArrayList<Student>();
        List params = new ArrayList();
        try {
            StringBuffer sqlbuf = new StringBuffer
                    (" select * from student where 1=1 and state!=4 ");
            //where恒成立，即当下面的模糊查找条件不成立时，做select *
            //不显示state为4的学生信息(被标记为删除)
            if (name != null && name.length() > 0) {
                sqlbuf.append(" and stuname like ? ");
                params.add("%" + name + "%");
            }
            if (stuno != null && stuno.length() > 0) {
                sqlbuf.append(" and stuno = ? ");
                params.add(stuno);
            }
            if (sex != -1) {
                sqlbuf.append(" and sex = ? ");
                params.add(sex);
            }

            //数据分页显示
            sqlbuf.append("limit ?,?");
            //与数组类似，limit参数从0算起，一个常用的式子：
            // limit (pageIndex-1)*pageSize,pageSize;
            params.add((pageIndex - 1) * pageSize);
            params.add(pageSize);

            ResultSet resultSet = query(sqlbuf.toString(), params);
            while (resultSet.next()) {
                Student student = new Student();
                student.setStuId(resultSet.getInt("stuid"));
                student.setStuNo(resultSet.getString("stuno"));
                student.setStuName(resultSet.getString("stuname"));
                student.setSex(resultSet.getInt("sex"));
                student.setPhone(resultSet.getString("phone"));
                student.setProfession(resultSet.getString("profession"));
                student.setRegDate(resultSet.getDate("regdate"));
                //补全所有列
                list.add(student);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            closeAll();
        }
        return list;
    }

    @Override
    public int total(String name, String stuno, int sex) {
        int total = 0;
        try {
            List params = new ArrayList();
            StringBuffer sqlbuf = new StringBuffer
                    (" select count(*) from student where 1=1 and state!=4 ");
            if (name != null && name.length() > 0) {
                sqlbuf.append(" and stuname like ? ");
                params.add("%" + name + "%");
            }
            if (stuno != null && stuno.length() > 0) {
                sqlbuf.append(" and stuno = ? ");
                params.add(stuno);
            }
            if (sex != -1) {
                sqlbuf.append(" and sex = ? ");
                params.add(sex);
            }
            resultSet = query(sqlbuf.toString(), params);
            while (resultSet.next()) {
                total = resultSet.getInt(1);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            closeAll();
        }
        return total;
    }

    @Override
    public int insertStudent(Student student) {
        int affectedEntries = 0;
        try {
            String sql = "insert into student values(null,?,?,?,?,?,?,?,?,?,?,?,?,?,?)";
            List params = new ArrayList();
            params.add(student.getStuName());
            params.add(student.getStuNo());
            params.add(student.getSex());
            params.add(student.getPhone());
            params.add(student.getEmail());
            params.add(student.getRegistered());
            params.add(student.getAddress());
            params.add(student.getProfession());
            params.add(student.getIdNumber());
            params.add(student.getPolitics());
            params.add(new Date());
            params.add(StudentEnum.READING.type);//1表示在读 (已使用枚举优化)
            params.add(student.getIntroduction());
            params.add(student.getGid());
            affectedEntries = update(sql, params);
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            closeAll();
        }
        return affectedEntries;
    }

    @Override
    public Student findById(int sid) {
        Student student = new Student();
        try {
            String sql = "select * from student where stuid=?";
            List params = new ArrayList();
            params.add(sid);
            resultSet = query(sql, params);
            while (resultSet.next()) {
                student.setStuId(resultSet.getInt("stuid"));
                student.setStuNo(resultSet.getString("stuno"));
                student.setStuName(resultSet.getString("stuname"));
                student.setSex(resultSet.getInt("sex"));
                student.setPhone(resultSet.getString("phone"));
                student.setProfession(resultSet.getString("profession"));
                student.setAddress(resultSet.getString("address"));
                student.setRegDate(resultSet.getDate("regdate"));
                student.setEmail(resultSet.getString("email"));
                student.setIntroduction(resultSet.getString("introduction"));
                student.setGid(resultSet.getInt("gid"));
                student.setRegistered(resultSet.getString("registered"));
                student.setIdNumber(resultSet.getString("idnumber"));
                student.setPolitics(resultSet.getString("politics"));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            closeAll();
        }
        return student;
    }

    @Override
    public int updateStudent(Student student) {
        int update = 0;
        try {
            String sql = "update student set stuname=?,stuno=?,sex=?,phone=?,email=?,registered=?" +
                    ",address=?,profession=?,idnumber=?,politics=?,state=?,introduction=?" +
                    "where stuid=?";
            List params = new ArrayList();
            params.add(student.getStuName());
            params.add(student.getStuNo());
            params.add(student.getSex());
            params.add(student.getPhone());
            params.add(student.getEmail());
            params.add(student.getRegistered());
            params.add(student.getAddress());
            params.add(student.getProfession());
            params.add(student.getIdNumber());
            params.add(student.getPolitics());
            params.add(student.getState());
            params.add(student.getIntroduction());
            params.add(student.getStuId());
            update = update(sql, params);
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            closeAll();
        }
        return update;
    }

    @Override
    public int deleteStudent(String sid) {
        int update = 0;
        try {
            String sql = "update student set state=? where stuid=?";
            List params = new ArrayList();
            params.add(StudentEnum.DELETE.type);
            params.add(sid);
            update = update(sql, params);
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            closeAll();
        }
        return update;
    }
}

