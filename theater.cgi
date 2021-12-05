#!/usr/bin/perl -w

use CGI qw(:standard -debug);
use CGI::Carp qw(fatalsToBrowser);

$action = param("action");
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
    print OUT $tName;
    close(OUT);
}


print header("Content-type: text/html; charset=utf-8");
print start_html();

foreach $theater (@theaters) {
    print "<p>$thater</p>";
}

print end_html();
