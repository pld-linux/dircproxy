Summary:	irc proxy
Summary(pl):	proxy irc
Name:		dircproxy
Version:	1.0.2
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://download.sourceforge.net/dircproxy/%{name}-%{version}.tar.gz
URL:		http://dircproxy.sourceforge.net/
BuildRequires:	autoconf
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
wykorzystuj±cych IRC z kilku ró¿nych komputerów lub programów, ale
chc±cych zostaæ po³±czonym i widzieæ co stracili gdy byli niedostêpni.
Pod³±czasz siê do IRC poprzez dircproxy a on trzyma ciebie
pod³±czonego do serwera nawet je¿eli siê od niego od³±czysz. Je¿eli
jestes od³±czony loguje kana³y i prywatne wiadomo¶ci jak równie¿ wa¿ne
zdarzenia i kiedy siê pod³±czasz pokazuje ci co straci³e¶.

%prep
%setup -q

%build
autoconf
%configure \
	--enable-poll
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog FAQ NEWS PROTOCOL README* TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/dircproxy/
%{_datadir}/dircproxy/*
%{_mandir}/man?/*
