#!/usr/bin/perl -w

use CGI qw(:standard -debug);
use CGI::Carp qw(fatalsToBrowser);

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
        color: black;
        font-family: 'Do Hyeon', sans-serif;
    }
    body {
        height : 1200px;
    }
    section {
        background-color: #FDFCF0;
        width: 100%;
        height: 100%;
    }
    h2 {
        padding: 20px;
        text-align : left;
        margin-left : 15%;
    }
    td {
        text-align : left;
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

@cgvTheater = (
    "CGV대구수성", "CGV대구스타디움", "CGV대구아카데미", "CGV대구연경", "CGV대구월성", 
    "CGV대구이시아", "CGV대구칠곡", "CGV대구한일", "CGV대구현대"
);
@cgvTheaterLink = (
    "http://www.cgv.co.kr/theaters/?areacode=11&theaterCode=0157&date=20211205",
    "http://www.cgv.co.kr/theaters/?areacode=11&theaterCode=0108&date=20211205",
    "http://www.cgv.co.kr/theaters/?areacode=11&theaterCode=0185&date=20211205",
    "http://www.cgv.co.kr/theaters/?areacode=11&theaterCode=0343&date=20211205",
    "http://www.cgv.co.kr/theaters/?areacode=11&theaterCode=0216&date=20211205",
    "http://www.cgv.co.kr/theaters/?areacode=11&theaterCode=0117&date=20211205",
    "http://www.cgv.co.kr/theaters/?areacode=11&theaterCode=0071&date=20211205",
    "http://www.cgv.co.kr/theaters/?areacode=11&theaterCode=0147&date=20211205",
    "http://www.cgv.co.kr/theaters/?areacode=11&theaterCode=0109&date=20211205"
);

$theaterCount = @cgvTheater;

print "</head>\n";
print "<html><body>";
print "<section>\n";
print h2("CGV 극장 (대구)");
print "<hr style = \"margin-left : 15%; margin-right : 15%;\">\n<table cellspacing=20px>\n";

open(IN, "theater.out");
@theaters = <IN>;
close(IN);

for ($i = 0; $i < $theaterCount; $i++) {
	$flag = 0;
    foreach $theater (@theaters) {
        if (substr($theater, 0, 3) eq "cgv" && substr($theater, 3, 1) eq $i) {
            $flag = 1;
        }
    }
	print "<tr>\n";
    print "<td class = link><a href = \"$cgvTheaterLink[$i]\" target = \"blank\">$cgvTheater[$i]</a></td>\n";
    if ($flag == 0) {
    	print "<td width = \"50px\" style = \"text-align : right;\"><a href = \"theater.cgi?name=cgv$i\">추가하기</a></td>\n";
    } else { 
	    print "<td></td>";
    }
    print "</tr>\n";
}
print "</table>\n</section>\n";
print "</html></body>";
print "\n\n";