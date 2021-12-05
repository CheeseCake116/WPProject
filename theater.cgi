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
    if ($theater eq $tName) {
        $flag = 1;
    }
}
if ($flag == 0) { # if tName is not exist
    open(OUT, ">>theater.out");
    print OUT "$tName\n";
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
@lotteTheater = (
    "롯데시네마 대구광장", "롯데시네마 대구율하", "롯데시네마 대구현풍", "롯데시네마 동성로", "롯데시네마 프리미엄만경", 
    "롯데시네마 성서", "롯데시네마 프리미엄칠곡", "롯데시네마 상인"
);
@megaTheater = (
    "메가박스 대구이시아", "메가박스 대구", "메가박스 대구신세계", "메가박스 북대구"
);

foreach $theater (@theaters) {
    print "<tr>\n";
    $index = substr($theater, 3, 1);
    if (substr($theater, 0, 3) eq "cgv") {
        print "<td>$cgvTheater[$index]</td>";
    } elsif (substr($theater, 0, 3) eq "meg") {
        print "<td>$megaTheater[$index]</td>";
    } elsif (substr($theater, 0, 3) eq "lot") {
        print "<td>$lotteTheater[$index]</td>";
    } else { 
        print "<td></td>";
    }

    print "</tr>\n";
}
print "</table></section>";
print "</html></body>";
print "\n\n";