<?php

namespace app;

class Controller19
{
    public function index()
    {
        // echo '我是Controller19的index()方法';
        require APP_PATH . 'Model19.php';
        $model = new Model19();
        $data = $model->getAll();
        // var_dump($data);
        require VIEW_PATH . 'View19.php';   // 引入视图文件
    }
}
