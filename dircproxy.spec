Summary:	irc proxy
Summary(pl):	proxy irc
Name:		dircproxy
Version:	1.0.0
Release:	1
License:	GPL
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
URL:		http://dircproxy.sourceforge.net/
Source0:	http://download.sourceforge.net/dircproxy/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dircproxy is an IRC proxy server designed for people who use IRC from
lots of different workstations or clients, but wish to remain
connected and see what they missed while they were away. You connect
to IRC through dircproxy, and it keeps you connected to the server,
even after you detach your client from it. While you're detached, it
logs channel and private messages as well as important events, and
when you reattach it'll let you know what you missed.

%description -l pl
dircproxy jest serwerem proxy IRC przeznaczonym dla ludzi
wykorzystuj�cych IRC z kilku r�nych komputer�w lub program�w, ale
chc�cych zosta� po��czonym i widzie� co stracili gdy byli niedost�pni.
Pod��czasz si� do IRC poprzez dircproxy a on trzyma ciebie
pod��czonego do serwera nawet je�eli si� od niego od��czysz. Je�eli
jestes od��czony loguje kana�y i prywatne wiadomo�ci jak r�wnie� wa�ne
zdarzenia i kiedy si� pod��czasz pokazuje ci co straci�e�.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT
gzip -9nf AUTHORS ChangeLog FAQ INSTALL NEWS PROTOCOL README* TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/dircproxy/
%{_datadir}/dircproxy/*
%{_mandir}/man?/*
%doc *.gz
