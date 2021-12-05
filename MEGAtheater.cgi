#!/usr/bin/perl -w

use CGI qw(:standard -debug);
use CGI::Carp qw(fatalsToBrowser);

print header("Content-type: text/html; charset=utf-8");
print "\n";
print start_html();
# print "<!DOCTYPE html>";
print "\n";
print "<head>\n";
print "<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">\n";
print  "<link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>\n";
print "<link href=\"https://fonts.googleapis.com/css2?family=Do+Hyeon&display=swap\" rel=\"stylesheet\">\n";
print "</head>\n";

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
        background-color: rgb(50, 33, 96);
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

@megaTheater = (
    "메가박스 대구이시아", "메가박스 대구", "메가박스 대구신세계", "메가박스 북대구"
);

@megaTheaterLink = (
    "https://www.megabox.co.kr/theater?brchNo=0022",
    "https://www.megabox.co.kr/theater?brchNo=7022",
    "https://www.megabox.co.kr/theater?brchNo=7011",
    "https://www.megabox.co.kr/theater?brchNo=0025"
);

$theaterCount = @megaTheater;

print "<section>\n";
print h2("메가박스 극장 (대구)");
print "<hr style = \"margin-left : 15%; margin-right : 15%;\">\n<table cellspacing=20px>\n";

open(IN, "theater.out");
@theaters = <IN>;
close(IN);

for ($i = 0; $i < $theaterCount; $i++) {
    $flag = 0;
    foreach $theater (@theaters) {
        if (substr($theater, 0, 3) eq "meg" && substr($theater, 3, 1) eq $i) {
            $flag = 1;
        }
    }
    print "<tr>\n<td><a href = \"$megaTheaterLink[$i]\" target = \"blank\">$megaTheater[$i]</a></td>\n";
    if ($flag == 0) {
    	print "<td width = \"50px\" style = \"text-align : right;\"><a href = \"theater.cgi?name=meg$i\">추가하기</td>\n";
    } else { 
	    print "<td></td>";
    }
    print "</tr>\n";
}
print "</table>\n</section>\n";
print end_html();
print "\n\n";