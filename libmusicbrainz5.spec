Summary:	A software library for accesing MusicBrainz servers
Name:		libmusicbrainz5
Version:	5.0.1
Release:	2
License:	LGPL v2
Group:		Libraries
Source0:	https://github.com/downloads/metabrainz/libmusicbrainz/libmusicbrainz-%{version}.tar.gz
# Source0-md5:	a0406b94c341c2b52ec0fe98f57cadf3
URL:		http://www.musicbrainz.org/
BuildRequires:	cmake
BuildRequires:	neon-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The MusicBrainz client library allows applications to make metadata
lookup to a MusicBrainz server, generate signatures from WAV data and
create CD Index Disk ids from audio CD roms.

%package devel
Summary:	Headers for developing programs that will use libmusicbrainz
Summary(pl.UTF-8):	Pliki nagłówkowe do rozwijania programów używających libmusicbrainz
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	neon-devel

%description devel
This package contains the headers that programmers will need to
develop applications which will use libmusicbrainz.

%prep
%setup -qn libmusicbrainz-%{version}

%build
%cmake .

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

chmod +x $RPM_BUILD_ROOT%{_libdir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS.txt NEWS.txt
%attr(755,root,root) %ghost %{_libdir}/libmusicbrainz5.so.?
%attr(755,root,root) %{_libdir}/libmusicbrainz5.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmusicbrainz5.so
%{_includedir}/musicbrainz5
%{_pkgconfigdir}/libmusicbrainz5.pc

