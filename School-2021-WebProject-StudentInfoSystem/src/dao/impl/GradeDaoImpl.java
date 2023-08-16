package dao.impl;

import bean.Grade;
import dao.GradeDao;
import util.DBUtils;

import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class GradeDaoImpl extends DBUtils implements GradeDao {
    @Override
    public List<Grade> getList() {
        ArrayList gradeList = new ArrayList();
        try {
            String sql = "select * from grade";
            resultSet = query(sql, null);
            while (resultSet.next()) {
                Grade grade = new Grade();
                grade.setGradeId(resultSet.getInt("gradeid"));
                grade.setGradeName(resultSet.getString("gradename"));
                gradeList.add(grade);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            closeAll();
        }
        return gradeList;
    }
}
