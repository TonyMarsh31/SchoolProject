package servlet;


import service.StudentService;
import service.impl.StudentServiceImpl;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;

@WebServlet("/Educational/student/deleteById")
public class DeleteByIdServlet extends HttpServlet {
    @Override
    protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {

        String sid = req.getParameter("sid");
        //根据主键查询学生信息
        StudentService service = new StudentServiceImpl();
        int i = service.deleteStudent(sid);
        resp.setContentType("text/html;charset=utf-8");
        PrintWriter writer = resp.getWriter();
        if (i > 0) {
            writer.println("<script>alert('删除成功');location.href='/Educational/student/StudentServlet'</script>");
        } else {
            writer.println("<script>alert('删除失败');location.href='/Educational/student/StudentServlet'</script>");
        }


    }
}
