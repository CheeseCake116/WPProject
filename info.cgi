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
    h3 {
        margin : 5px;
    }
    h4 {
        margin : 5px;
    }
    a {
        margin : 5px;
    }
    .link {
        padding : 5px;
        margin-top : 10px;
        background-color : rgba(0, 0, 0, 0.4);
    }
    .link:hover {
        background-color : rgba(0, 0, 0, 0.6);
    }
</style>
EOP
print "</head>\n";
print "<html><body>";
print "<section>";
print h2("About us");
print "<hr style = \"margin-left : 15%; margin-right : 15%;\">\n";
print "<table cellspacing=30px>";
print "<tr>";
print "<td><div>";
print "<img src=\"images/Jinuk_Kwak-icon.png\" style = \"box-sizing: inherit;\">";
print h3("Jinuk Kwak");
print h4("7ehrtnfl\@naver.com");
print "<br><a href=\"http://widit.knu.ac.kr/~7ehrtnfl/ithw/hw5-1.htm\" class = link>personal page</a>";
print "</div></td>";

print "<td><div>";
print "<img src=\"images/Hyoeun_Sim-icon.png\" style = \"box-sizing: inherit;\">";
print h3("Hyoeun Sim");
print h4("f2921641\@naver.com");
print "<br><a href=\"http://widit.knu.ac.kr/~f2921641/ithw/hw5.htm\" class = link>personal page</a>";
print "</div></td>";

print "<td><div>";
print "<img src=\"images/Gyurim_Park-icon.png\" style = \"box-sizing: inherit;\">";
print h3("Gyurim Park");
print h4("guy021898\@naver.com");
print "<br><a href=\"http://widit.knu.ac.kr/~guy021898/ithw/hw5.htm\" class = link>personal page</a>";
print "</div></td>";
print "</tr>";
print "</table>\n";

print h2("Source code");
print "<hr style = \"margin-left : 15%; margin-right : 15%;\">\n";
print "<a href = \"https://github.com/CheeseCake116/WPProject\" target = \"blank\" style = \"float: left; margin-left : 20%; margin-top : 20px;\">";
print "<img src = \"images/github.jpg\" width = 160px></a>";

print "</section>\n</html></body>";
print "\n\n";