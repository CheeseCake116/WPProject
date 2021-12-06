#!/usr/bin/perl -w

use CGI qw(:standard -debug);
use CGI::Carp qw(fatalsToBrowser);

$tName = param("name");

open(IN, "theater.out");
@theaters = <IN>;
close(IN);
chomp @theaters;

$flag = 0; # test whether exist or not
foreach $theater (@theaters) {
    if ($theater eq $tName || $tName eq "null") {
        $flag = 1;
    }
}
if (substr($tName, 0, 3) eq "del") {
    $flag = 2;
}

if ($flag == 0) { # if tName is not exist
    open(OUT, ">>theater.out");
    print OUT "$tName\n";
    close(OUT);
}
if ($flag == 2) { # wanna delete
    open(OUT, ">theater.out");
    foreach $name (@theaters) {
        chomp $name;
        if ($name ne substr($tName, 3, 4)) {
            print OUT "$name\n";
        }
    }
    close(OUT);
}

# background-color : slategray;
print header("Content-type: text/html; charset=utf-8");
print "<head>\n";
print "<title>Untitled Document</title>";
print "<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">\n";
print "<link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>\n";
print "<link href=\"https://fonts.googleapis.com/css2?family=Do+Hyeon&display=swap\" rel=\"stylesheet\">\n";
print <<EOP;
<style>
    * {
        margin: 0;
        padding: 0;
        text-align: center;
        color: white;
        font-family: 'Do Hyeon', sans-serif;        
    }
    body {
        height : 1200px;
    }
    section {
        background-color: slategray;
        width: 100%;
        height: 100%;
    }
    h2 {
        padding: 20px;
        text-align : left;
        margin-left : 15%;
    }
    table {
        width : 70%;
        margin : auto;
    }
    td {
        padding : 10px;
        text-align : left;
        background-color : rgba(0, 0, 0, 0);
    }
    td:hover {
        background-color : rgba(0, 0, 0, 0.2);
    }
</style>
EOP
print "</head>\n";
print "<html><body>";
print "<section>";
print h2("My Theaters");
print "<hr style = \"margin-left : 15%; margin-right : 15%;\">\n<table cellspacing=30px>";

@cgvTheater = (
    "CGV대구수성", "CGV대구스타디움", "CGV대구아카데미", "CGV대구연경", "CGV대구월성", 
    "CGV대구이시아", "CGV대구칠곡", "CGV대구한일", "CGV대구현대"
);
@cgvTheaterWay = (
    "https://map.naver.com/v5/?c=14320190.3578971,4276037.1584801,15,0,0,0,dh&lng=128.6404587&lat=35.8211314&type=0&title=CGV%EB%8C%80%EA%B5%AC%EC%88%98%EC%84%B1",
    "https://map.naver.com/v5/?c=14325898.4030976,4277204.0565060,15,0,0,0,dh&lng=128.69173494246&lat=35.829630597172&type=0&title=CGV%EB%8C%80%EA%B5%AC%EC%8A%A4%ED%83%80%EB%94%94%EC%9B%80",
    "https://map.naver.com/v5/?c=14315052.5849107,4282746.6363320,15,0,0,0,dh&lng=128.5943053&lat=35.869988&type=0&title=CGV%EB%8C%80%EA%B5%AC%EC%95%84%EC%B9%B4%EB%8D%B0%EB%AF%B8",
    "https://map.naver.com/v5/?c=14318220.6973823,4292561.1968864,15,0,0,0,dh&lng=128.62276493855003&lat=35.941400738412334&type=0&title=CGV%EB%8C%80%EA%B5%AC%EC%97%B0%EA%B2%BD",
    "https://map.naver.com/v5/?c=14307473.8203941,4276492.1120816,15,0,0,0,dh&lng=128.52622410000004&lat=35.8244452&type=0&title=CGV%EB%8C%80%EA%B5%AC%EC%9B%94%EC%84%B1",
    "https://map.naver.com/v5/?c=14319831.3414074,4289806.1137833,15,0,0,0,dh&lng=128.6372336&lat=35.9213607&type=0&title=CGV%EB%8C%80%EA%B5%AC%EC%9D%B4%EC%8B%9C%EC%95%84",
    "https://map.naver.com/v5/?c=14311228.3596518,4292933.5518775,15,0,0,0,dh&lng=128.5599517&lat=35.9441088&type=0&title=CGV%EB%8C%80%EA%B5%AC%EC%B9%A0%EA%B3%A1",
    "https://map.naver.com/v5/?c=14315169.6484873,4282813.8253490,15,0,0,0,dh&lng=128.5953569&lat=35.8704771&type=0&title=CGV%EB%8C%80%EA%B5%AC%ED%95%9C%EC%9D%BC",
    "https://map.naver.com/v5/?c=14314638.5988564,4282305.0756503,15,0,0,0,dh&lng=128.5905864&lat=35.8667736&type=0&title=CGV%EB%8C%80%EA%B5%AC%ED%98%84%EB%8C%80"
);
@lotteTheater = (
    "롯데시네마 대구광장", "롯데시네마 대구율하", "롯데시네마 대구현풍", "롯데시네마 동성로", "롯데시네마 프리미엄만경", 
    "롯데시네마 성서", "롯데시네마 프리미엄칠곡", "롯데시네마 상인"
);
@lotteTheaterWay = (
    "https://map.naver.com/v5/search/%EB%A1%AF%EB%8D%B0%EC%8B%9C%EB%84%A4%EB%A7%88%20%EB%8C%80%EA%B5%AC%EA%B4%91%EC%9E%A5?c=14309733.9511477,4280786.8392015,15,0,0,0,dh",
    "https://map.naver.com/v5/search/%EB%A1%AF%EB%8D%B0%EC%8B%9C%EB%84%A4%EB%A7%88%20%EB%8C%80%EA%B5%AC%EC%9C%A8%ED%95%98?c=14325682.2159198,4282482.6923251,15,0,0,0,dh",
    "https://map.naver.com/v5/search/%EB%A1%AF%EB%8D%B0%EC%8B%9C%EB%84%A4%EB%A7%88%20%EB%8C%80%EA%B5%AC%ED%98%84%ED%92%8D/place/1940488737?c=14299221.1388122,4258491.7891086,15,0,0,0,dh",
    "https://map.naver.com/v5/search/%EB%A1%AF%EB%8D%B0%EC%8B%9C%EB%84%A4%EB%A7%88%20%EB%8F%99%EC%84%B1%EB%A1%9C/place/12869933?c=14314881.4757214,4283275.9310751,15,0,0,0,dh&placePath=%3Fentry%253Dbmp",
    "https://map.naver.com/v5/search/%EB%A1%AF%EB%8D%B0%EC%8B%9C%EB%84%A4%EB%A7%88%20%ED%94%84%EB%A6%AC%EB%AF%B8%EC%97%84%EB%A7%8C%EA%B2%BD/place/1362567570?c=14313681.3514231,4282879.8608389,15,0,0,0,dh",
    "https://map.naver.com/v5/search/%EB%A1%AF%EB%8D%B0%EC%8B%9C%EB%84%A4%EB%A7%88%20%EC%84%B1%EC%84%9C/place/12299945?c=14304952.8012820,4280626.1986220,15,0,0,0,dh&placePath=%3Fentry%253Dbmp",
    "https://map.naver.com/v5/search/%EB%A1%AF%EB%8D%B0%EC%8B%9C%EB%84%A4%EB%A7%88%20%ED%94%84%EB%A6%AC%EB%AF%B8%EC%97%84%20%EC%B9%A0%EA%B3%A1/place/13437593?c=14311202.2440993,4292680.8140965,15,0,0,0,dh&placePath=%3Fentry%253Dbmp",
    "https://map.naver.com/v5/search/%EB%A1%AF%EB%8D%B0%EC%8B%9C%EB%84%A4%EB%A7%88%08%20%EC%83%81%EC%9D%B8/place/37397527?c=14308470.9869968,4275401.3700552,15,0,0,0,dh"
);
@megaTheater = (
    "메가박스 대구이시아", "메가박스 대구", "메가박스 대구신세계", "메가박스 북대구"
);
@megaTheaterWay = (
    "https://m.map.naver.com/map.naver?lng=128.635719&lat=35.920749&level=1",
    "https://m.map.naver.com/map.naver?lng=128.5897973&lat=35.885178&level=1",
    "https://m.map.naver.com/map.naver?lng=128.6294&lat=35.877686&level=1",
    "https://m.map.naver.com/map.naver?lng=128.561734&lat=35.9440731&level=1"
);

open(IN, "theater.out");
@theaters = <IN>;
close(IN);
chomp @theaters;

foreach $theater (@theaters) {
    print "<tr>\n";
    $index = substr($theater, 3, 1);
    if (substr($theater, 0, 3) eq "cgv") {
        print "<td>$cgvTheater[$index]</td>\n";
        print "<td width = \"40px\" style = \"text-align : right;\"><a href = \"$cgvTheaterWay[$index]\" target = \"blank\">길찾기</a></td>";
    } elsif (substr($theater, 0, 3) eq "meg") {
        print "<td>$megaTheater[$index]</td>";
        print "<td width = \"40px\" style = \"text-align : right;\"><a href = \"$megaTheaterWay[$index]\" target = \"blank\">길찾기</a></td>";
    } elsif (substr($theater, 0, 3) eq "lot") {
        print "<td>$lotteTheater[$index]</td>";
        print "<td width = \"40px\" style = \"text-align : right;\"><a href = \"$lotteTheaterWay[$index]\" target = \"blank\">길찾기</a></td>";
    } else { 
        print "<td></td>";
    }
    print "<td width = \"40px\" style = \"text-align : right;\"><a href = \"theater.cgi?name=del$theater\">삭제</a></td>\n";
    print "</tr>\n";
}
print "</table></section>";
print "</html></body>";
print "\n\n";