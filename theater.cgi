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
if ($flag == 0) {
    open(OUT, ">>theater.out");
    print OUT "$tName\n";
    close(OUT);
}

# background-color : slategray;
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



print "<section>";
print h2("My Theaters");
print "<hr style = \"margin-left : 15%; margin-right : 15%;\">\n<table cellspacing=30px>";

foreach $theater (@theaters) {
    print "<tr>\n";
    print "<td>$theater</td>";
    print "</tr>\n";
}
print "</table></section>";
print end_html();
print "\n\n";