Summary:	irc proxy
Summary(pl.UTF-8):   proxy irc
Name:		dircproxy
Version:	1.0.5
Release:	2
License:	GPL
Group:		Applications/Communications
Source0:	ftp://ftp.dircproxy.net/pub/dircproxy/1.0/%{name}-%{version}.tar.gz
# Source0-md5:	33b92e0f28530a5faa9fea801d1ad807
Patch0:		%{name}-ac_fix.patch
URL:		http://www.dircproxy.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dircproxy is an IRC proxy server designed for people who use IRC from
lots of different workstations or clients, but wish to remain
connected and see what they missed while they were away. You connect
to IRC through dircproxy, and it keeps you connected to the server,
even after you detach your client from it. While you're detached, it
logs channel and private messages as well as important events, and
when you reattach it'll let you know what you missed.

%description -l pl.UTF-8
dircproxy jest serwerem proxy IRC przeznaczonym dla ludzi
wykorzystujących IRC z kilku różnych komputerów lub programów, ale
chcących zostać połączonym i widzieć co stracili gdy byli niedostępni.
Podłączasz się do IRC poprzez dircproxy a on trzyma ciebie podłączonego 
do serwera nawet jeżeli się od niego odłączysz. Jeżeli jesteś odłączony 
loguje kanały i prywatne wiadomości jak również ważne zdarzenia i kiedy 
się podłączasz pokazuje ci co straciłeś.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-poll
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ NEWS PROTOCOL README*
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/dircproxy/
%{_datadir}/dircproxy/*
%{_mandir}/man?/*
