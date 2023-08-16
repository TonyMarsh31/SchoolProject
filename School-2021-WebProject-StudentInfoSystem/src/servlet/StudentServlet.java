package servlet;

import bean.Student;
import service.StudentService;
import service.impl.StudentServiceImpl;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.List;

@WebServlet("/Educational/student/StudentServlet")
public class StudentServlet extends HttpServlet {
    @Override
    protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        //1. 获取参数
        //下面的参数用于模糊查找
        String stuname = req.getParameter("stuname");
        String stuno = req.getParameter("stuno");
        String sex_temp = req.getParameter("sex");
        //将sex的数据类型转从String转换成int
        int sex = (sex_temp == null || sex_temp.length() == 0
                ? -1 : Integer.parseInt(sex_temp));// 避免Integer.parseInt方法报错

        //下面的参数用于数据的分页显示 (sql:limit 开始位置 显示条目数)
        //页码值：
        String pageIndex = req.getParameter("pageIndex");
        //如果页面没有传入pageIndex的值，则默认查询第一页的数据
        int index = pageIndex == null ? 1 : Integer.parseInt(pageIndex);

        //2. 调用Service层
        StudentService studentService = new StudentServiceImpl();
        //显示学生信息
        List<Student> students = studentService.getStudents
                (stuname, stuno, sex, index, 5);

        //获取显示显示条目的总页数
        //总页数=总条目数%每页显示的条数>0?总条数/每页显示条数+1：总条数/每页显示条数
        //每页显示的条目数pageSize被手动设定 所以需要动态获取的是总条目数
        int total = studentService.total(stuname, stuno, sex);//总条目数
        int size = 5;//每页显示的条目数
        int totalPages = total % size > 0 ? total / size + 1 : total / size;//总页数


        //向前台发送数据
        req.setAttribute("stulist", students);

        //存储模糊查询的条件
        req.setAttribute("stuname", stuname);
        req.setAttribute("stuno", stuno);
        req.setAttribute("sex", sex);

        //存储分页展示数据的相关设置数据
        req.setAttribute("index", index);
        req.setAttribute("size", size);
        req.setAttribute("total", total);
        req.setAttribute("totalPages", totalPages);

        //3. 跳转页面
        req.getRequestDispatcher("list.jsp").forward(req, resp);//本Servlet的url中已经有Educational/student/的前缀
    }
}
