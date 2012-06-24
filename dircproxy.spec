Summary:	irc proxy
Summary(pl):	proxy irc
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

%description -l pl
dircproxy jest serwerem proxy IRC przeznaczonym dla ludzi
wykorzystuj�cych IRC z kilku r�nych komputer�w lub program�w, ale
chc�cych zosta� po��czonym i widzie� co stracili gdy byli niedost�pni.
Pod��czasz si� do IRC poprzez dircproxy a on trzyma ciebie pod��czonego 
do serwera nawet je�eli si� od niego od��czysz. Je�eli jeste� od��czony 
loguje kana�y i prywatne wiadomo�ci jak r�wnie� wa�ne zdarzenia i kiedy 
si� pod��czasz pokazuje ci co straci�e�.

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
