package servlet;

import bean.Users;
import service.UsersService;
import service.impl.UsersServiceImpl;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;

@WebServlet("/login")
public class LoginServlet extends HttpServlet {

    @Override
    protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        //1.接受参数
        String username = req.getParameter("username");
            String password = req.getParameter("password");
        //2.调用Service层
        UsersService usersService = new UsersServiceImpl();
        Users users = usersService.login(username, password);
        //3.跳转页面
        if (users == null) {
            //以弹窗的方式提示用户登陆失败
            resp.setContentType("text/html;charset=utf-8");
            PrintWriter writer = resp.getWriter();
            writer.println("<script>location.href='login.jsp';alert('用户名或密码不正确');</script>");
        } else {
            //跳转到系统的主页面
            //保存用户信息
            req.getSession().setAttribute("users",users);
            resp.sendRedirect("index.jsp");
        }
    }
}
