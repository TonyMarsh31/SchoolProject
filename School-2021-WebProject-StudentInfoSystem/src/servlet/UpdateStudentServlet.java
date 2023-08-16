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
import java.io.PrintWriter;

@WebServlet(urlPatterns = "/Educational/student/updateStudent")
public class UpdateStudentServlet extends HttpServlet {
    @Override
    protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        //接收参数 与addStudentServlet中一样
        String sid = req.getParameter("sid");
        String stuNo = req.getParameter("stuNo");
        String stuName = req.getParameter("stuName");
        String sex = req.getParameter("sex");
        String state_temp = req.getParameter("state");
        int state = (state_temp == null || state_temp.length() == 0
                ? 1 : Integer.parseInt(state_temp));// 避免Integer.parseInt方法报错
        String email = req.getParameter("email");
        String phone = req.getParameter("phone");
        String registered = req.getParameter("registered");
        String address = req.getParameter("address");
        String politics = req.getParameter("politics");
        String idNumber = req.getParameter("idNumber");
        String profession = req.getParameter("profession");
        String introduction = req.getParameter("introduction");

        //将参数封装给Student
        Student stu = new Student();
        stu.setStuId(Integer.parseInt(sid));
        stu.setStuName(stuName);
        stu.setStuNo(stuNo);
        stu.setSex(Integer.parseInt(sex));
        stu.setPhone(phone);
        stu.setEmail(email);
        stu.setRegistered(registered);
        stu.setAddress(address);
        stu.setProfession(profession);
        stu.setIdNumber(idNumber);
        stu.setPolitics(politics);
        stu.setState(state);
        stu.setIntroduction(introduction);

        //调用Service层
        StudentService service = new StudentServiceImpl();
        int i = service.updateStudent(stu);

        //跳转页面
        resp.setContentType("text/html;charset=utf-8");
        PrintWriter writer = resp.getWriter();
        if (i > 0) {
            writer.println("<script>alert('更新成功');location.href='/Educational/student/StudentServlet'</script>");
        } else {
            writer.println("<script>alert('更新失败');location.href='/Educational/student/findById?sid=" + sid + "'</script>");
        }

    }
}
