<?php


use app\Controller19;

const APP_PATH = '../app/';
const VIEW_PATH = '../views/';
require APP_PATH . 'Controller19.php';
$books = new Controller19();
$books->index();
