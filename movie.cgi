#!/usr/bin/perl -w

use CGI qw(:standard -debug);
use CGI::Carp qw(fatalsToBrowser);

$mName = param("name");

open(IN, "movie.out");
@movies = <IN>;
close(IN);
chomp @movies;

$flag = 0; # test whether exist or not
foreach $movie (@movies) {
    if ($movie eq $mName || $mName eq "null") {
        $flag = 1;
    }
}
if (substr($mName, 0, 3) eq "del") {
    $flag = 2;
}

if ($flag == 0) { # if tName is not exist
    open(OUT, ">>movie.out");
    print OUT "$mName\n";
    close(OUT);
}
if ($flag == 2) { # wanna delete
    open(OUT, ">movie.out");
    foreach $name (@movies) {
        chomp $name;
        if ($name ne substr($mName, 3, 4)) {
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
print h2("Movie Wishlist");
print "<hr style = \"margin-left : 15%; margin-right : 15%;\">\n<table cellspacing=30px>";

@cgvMovieName = (
    "???", "????????? - ????????? ??????", "?????? ?????? ?????????", "???????????????",
    "????????????????????? ?????????", "????????? ?????? ??? ??????", "?????????", "????????? ????????????"
);
@cgvMoviePoster = (
    "https://img.cgv.co.kr/Movie/Thumbnail/Poster/000084/84945/84945_1000.jpg",
    "https://img.cgv.co.kr/Movie/Thumbnail/Poster/000085/85121/85121_1000.jpg",
    "https://img.cgv.co.kr/Movie/Thumbnail/Poster/000085/85239/85239_1000.jpg",
    "https://img.cgv.co.kr/Movie/Thumbnail/Poster/000083/83105/83105_1000.jpg",

    "https://img.cgv.co.kr/Movie/Thumbnail/Poster/000083/83033/83033_320.jpg",
    "https://img.cgv.co.kr/Movie/Thumbnail/Poster/000085/85261/85261_320.jpg",
    "https://img.cgv.co.kr/Movie/Thumbnail/Poster/000085/85125/85125_320.jpg",
    "https://img.cgv.co.kr/Movie/Thumbnail/Poster/000085/85234/85234_320.jpg"
);
@cgvMovieLink = (
    "http://www.cgv.co.kr/movies/detail-view/?midx=84945",
    "http://www.cgv.co.kr/movies/detail-view/?midx=85121",
    "http://www.cgv.co.kr/movies/detail-view/?midx=85239",
    "http://www.cgv.co.kr/movies/detail-view/?midx=83105",

    "http://www.cgv.co.kr/movies/detail-view/?midx=83033",
    "http://www.cgv.co.kr/movies/detail-view/?midx=85261",
    "http://www.cgv.co.kr/movies/detail-view/?midx=85125",
    "http://www.cgv.co.kr/movies/detail-view/?midx=85234"
);
@lotteMovieName = (
    "???????????????", "?????? ?????? ?????????", "?????????: ????????? ??????", "????????????????????? ?????????",
    "???", "????????????", "????????????", "????????? ?????? ??? ??????"
);
@lotteMoviePoster = (
    "https://caching.lottecinema.co.kr//Media/MovieFile/MovieImg/202111/18093_103_1.jpg",
    "https://caching.lottecinema.co.kr//Media/MovieFile/MovieImg/202111/18081_103_1.jpg",
    "https://caching.lottecinema.co.kr//Media/MovieFile/MovieImg/202111/18041_103_1.jpg",
    "https://caching.lottecinema.co.kr//Media/MovieFile/MovieImg/202007/15368_103_1.jpg",
    "https://caching.lottecinema.co.kr//Media/MovieFile/MovieImg/202110/17864_103_1.jpg",
    "https://caching.lottecinema.co.kr//Media/MovieFile/MovieImg/202111/18064_103_1.jpg",
    "https://caching.lottecinema.co.kr//Media/MovieFile/MovieImg/202111/17885_103_1.jpg",
    "https://caching.lottecinema.co.kr//Media/MovieFile/MovieImg/202112/18156_103_1.jpg"
);
@lotteMovieLink = (
    "https://www.lottecinema.co.kr/NLCHS/Movie/MovieDetailView?movie=18093",
    "https://www.lottecinema.co.kr/NLCHS/Movie/MovieDetailView?movie=18081",
    "https://www.lottecinema.co.kr/NLCHS/Movie/MovieDetailView?movie=18041",
    "https://www.lottecinema.co.kr/NLCHS/Movie/MovieDetailView?movie=15368",
    "https://www.lottecinema.co.kr/NLCHS/Movie/MovieDetailView?movie=17864",
    "https://www.lottecinema.co.kr/NLCHS/Movie/MovieDetailView?movie=18064",
    "https://www.lottecinema.co.kr/NLCHS/Movie/MovieDetailView?movie=17885",
    "https://www.lottecinema.co.kr/NLCHS/Movie/MovieDetailView?movie=18156"
);
@megaMovieName = (
    "?????? ?????????: ????????? ?????????", "??? ??? ???", "?????????", "????????? ?????????",
    "???????????????", "????????????????????? ?????????", "????????? ?????? ??? ??????", "?????????"    
);
@megaMoviePoster = (
    "https://img.megabox.co.kr/SharedImg/2021/11/19/OSwPwX3tSSnxJZMGljSs2tZESq6uFliO_420.jpg",
    "https://img.megabox.co.kr/SharedImg/2021/12/02/E3UIW76SDtxGcGAOqHD7ZsXcJ0y856tf_420.jpg",
    "https://img.megabox.co.kr/SharedImg/2021/12/02/j3wKuMLP0OjyE7PBNqDfcmzUGEtv9l9e_420.jpg",
    "https://img.megabox.co.kr/SharedImg/2021/11/01/JSLiuBzfSh0944XsetBXVFZSSaXfPjO6_420.jpg",
    "https://img.megabox.co.kr/SharedImg/2021/11/03/tP5BVdJ82rerjg37crDMrNpehEFcPfuZ_420.jpg",
    "https://img.megabox.co.kr/SharedImg/2021/11/12/ZL6rOSUwTNgWJLdJ0RM58Y4IsVs8m77h_420.jpg",
    "https://img.megabox.co.kr/SharedImg/2021/11/08/3ZcfD8ozZSG8r0uGKs1Aib4h7u6Gb0ZF_420.jpg",
    "https://img.megabox.co.kr/SharedImg/2021/11/26/UgC0ynJIDkgMHevC4Z1c4isRIRsjsUMT_420.jpg",
);
@megaMovieLink = (
    "https://www.megabox.co.kr/movie-detail?rpstMovieNo=21061000",
    "https://www.megabox.co.kr/movie-detail?rpstMovieNo=21086300",
    "https://www.megabox.co.kr/movie-detail?rpstMovieNo=21075400",
    "https://www.megabox.co.kr/movie-detail?rpstMovieNo=21073200",
    "https://www.megabox.co.kr/movie-detail?rpstMovieNo=21075100",
    "https://www.megabox.co.kr/movie-detail?rpstMovieNo=01675700",
    "https://www.megabox.co.kr/movie-detail?rpstMovieNo=21077200",
    "https://www.megabox.co.kr/movie-detail?rpstMovieNo=21086000"
);

open(IN, "movie.out");
@movies = <IN>;
close(IN);
chomp @movies;

$colCount = 1;
print "<tr>\n";
foreach $movie (@movies) {
    $index = substr($movie, 3, 1);
    if (substr($movie, 0, 3) eq "cgv") {
        print "<td>\n<image src = \"$cgvMoviePoster[$index]\">\n</td>\n";
        print "<td style = \"width : 200px;\">\n<p>CGV</p><p style = \"margin : 10px; font-size : 100%;\">$cgvMovieName[$index]</p><hr><br><br>\n";
        print "<p class = link><a href = \"$cgvMovieLink[$index]\" target = \"blank\">????????????</a></p><br>\n";
        print "<p class = link><a href = \"movie.cgi?name=del$movie\">??????</a></p>\n</td><td></td>\n";
    } elsif (substr($movie, 0, 3) eq "meg") {
        print "<td>\n<image src = \"$megaMoviePoster[$index]\">\n</td>\n";
        print "<td style = \"width : 200px;\">\n<p>MEGABOX</p><p style = \"margin : 10px; font-size : 100%;\">$megaMovieName[$index]</p><hr><br><br>\n";
        print "<p class = link><a href = \"$megaMovieLink[$index]\" target = \"blank\">????????????</a></p><br>\n";
        print "<p class = link><a href = \"movie.cgi?name=del$movie\">??????</a></p>\n</td><td></td>\n";
    } elsif (substr($movie, 0, 3) eq "lot") {
        print "<td>\n<image src = \"$lotteMoviePoster[$index]\">\n</td>\n";
        print "<td style = \"width : 200px;\">\n<p>LOTTE CINEMA</p><p style = \"margin : 10px; font-size : 100%;\">$lotteMovieName[$index]</p><hr><br><br>\n";
        print "<p class = link><a href = \"$lotteMovieLink[$index]\" target = \"blank\">????????????</a></p><br>\n";
        print "<p class = link><a href = \"movie.cgi?name=del$movie\">??????</a></p>\n</td><td></td>\n";
    } else { 
        print "<td></td>";
    }
    #print "<td width = \"40px\" style = \"text-align : right;\"><a href = \"movie.cgi?name=del$movie\">??????</a></td>\n";
    if ($colCount % 2 == 0) {
        print "</tr><tr>";
    }
    $colCount++;
}
print "</tr>\n";
print "</table></section>";
print "</html></body>";
print "\n\n";