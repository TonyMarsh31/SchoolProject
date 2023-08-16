package servlet;

import bean.Grade;
import bean.Student;
import service.GradeService;
import service.StudentService;
import service.impl.GradeServiceImpl;
import service.impl.StudentServiceImpl;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.List;

@WebServlet("/Educational/student/findById")
public class FindByIdServlet extends HttpServlet {
    @Override
    protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        //接受参数
        String sid = req.getParameter("sid");

        //根据主键查询学生信息
        StudentService service = new StudentServiceImpl();
        Student student = service.findById(Integer.parseInt(sid));
        req.setAttribute("stu", student);

        //查询年级列表
        GradeService gradeService = new GradeServiceImpl();
        List<Grade> list = gradeService.getList();
        req.setAttribute("glist", list);

        req.getRequestDispatcher("edit.jsp").forward(req, resp);

    }
}
