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
print h2("Movie Wishlist");
print "<hr style = \"margin-left : 15%; margin-right : 15%;\">\n<table cellspacing=30px>";

@cgvMovieName = (
    "듄", "엘칸토 - 마법의 세계", "연애 빠진 로맨스", "유체이탈자",
    "고스트버스터즈 라이즈", "라스트 나잇 인 소호", "태일이", "프렌치 디스패치"
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
@lotteMovieName = (
    "유체이탈자", "연애 빠진 로맨스", "엔칸토: 마법의 세계", "고스트버스터즈 라이즈",
    "듄", "베네데타", "이터널스", "라스트 나잇 인 소호"
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
@megaMovieName = (
    "킬링 카인드: 킬러의 수제자", "돈 룩 업", "태일이", "너에게 가는길",
    "고스트버스터즈 라이즈", "유체이탈자", "라스트 나잇 인 소호", "언힐러"    
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

open(IN, "movie.out");
@movies = <IN>;
close(IN);
chomp @movies;

foreach $movie (@movies) {
    print "<tr>\n";
    $index = substr($movie, 3, 1);
    if (substr($movie, 0, 3) eq "cgv") {
        print "<td>$cgvMovieName[$index]</td>";
    } elsif (substr($movie, 0, 3) eq "meg") {
        print "<td>$megaMovieName[$index]</td>";
    } elsif (substr($movie, 0, 3) eq "lot") {
        print "<td>$lotteMovieName[$index]</td>";
    } else { 
        print "<td></td>";
    }
    print "<td width = \"40px\" style = \"text-align : right;\"><a href = \"movie.cgi?name=del$movie\">삭제</a></td>\n";
    print "</tr>\n";
}
print "</table></section>";
print "</html></body>";
print "\n\n";