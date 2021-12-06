#!/usr/bin/perl -w

use CGI qw(:standard -debug);
use CGI::Carp qw(fatalsToBrowser);

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
    img {
        width: 200px;
    }
    img:hover {
        background-color : rgba(0, 0, 0, 0.2);
    }
    .link {
            background-color : rgba(0, 0, 0, 0.2);
    }
    .link:hover {
        background-color : rgba(0, 0, 0, 0.5);
    }
    td {
        text-align : left;
        background-color : rgba(0, 0, 0, 0);
    }
</style>
EOP
print "</head>\n";
print "<html><body>";
print "<section>";
print h2("Information");
print "<hr style = \"margin-left : 15%; margin-right : 15%;\">\n";
print "<table cellspacing=30px>";
print "<tr><td colspan = '3' style = \"text-algin : left;\">";
print h3("About us");
print "</td></tr>\n";

print "<tr>";
print "<td><div>";
print "<img src=\"images/Jinuk_Kwak-icon.png\" style = \"box-sizing: inherit;\">";
print h3("Jinuk Kwak");
print h4("7ehrtnfl\@naver.com");
print "<a href=\"http://widit.knu.ac.kr/~7ehrtnfl/ithw/hw5-1.htm\">personal page</a>";
print "</div></td>"

print "<td><div>";
print "<img src=\"images/Hyoeun_Sim-icon.png\" style = \"box-sizing: inherit;\">";
print h3("Hyoeun Sim");
print h4("f2921641\@naver.com");
print "<a href=\"http://widit.knu.ac.kr/~f2921641/ithw/hw5.htm\">personal page</a>";
print "</div></td>"

print "<td><div>";
print "<img src=\"images/Gyurim_Park-icon.png\" style = \"box-sizing: inherit;\">";
print h3("Gyurim Park");
print h4("guy021898\@naver.com");
print "<a href=\"http://widit.knu.ac.kr/~guy021898/ithw/hw5.htm\">personal page</a>";
print "</div></td>"
print "</tr>";

print "<tr>";
print "<hr style = \"margin-left : 15%; margin-right : 15%;\">\n";
print "<td><td colspan = '3' style = \"text-algin : left;\">";
print h3("Source code");
print "</td>";
print "</tr>";

print "</html></body>";
print "\n\n";