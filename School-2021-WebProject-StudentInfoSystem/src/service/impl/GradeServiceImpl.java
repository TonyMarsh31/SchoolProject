package service.impl;

import bean.Grade;
import dao.GradeDao;
import dao.impl.GradeDaoImpl;
import service.GradeService;

import java.util.List;

public class GradeServiceImpl implements GradeService {
    private GradeDao gradeDao = new GradeDaoImpl();

    @Override
    public List<Grade> getList() {
        return gradeDao.getList();
    }
}
