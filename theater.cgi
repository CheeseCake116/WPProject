#!/usr/bin/perl -w

use CGI qw(:standard -debug);
use CGI::Carp qw(fatalsToBrowser);

$tName = param("name");

print header("Content-type: text/html; charset=utf-8");
print start_html();

print "<b>$tName</b>";

print end_html();
