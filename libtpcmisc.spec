Summary:	PET Miscellaneous library
Summary(pl.UTF-8):	Biblioteka PET Miscellaneous
Name:		libtpcmisc
Version:	1.3.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.turkupetcentre.net/software/libsrc/%{name}_%(echo %{version} | tr . _)_src.zip
# Source0-md5:	2ef27f792615bbc2600c9254be79c6a5
Patch0:		%{name}-shared.patch
URL:		http://www.turkupetcentre.net/software/libdoc/libtpcmisc/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PET Miscellaneous library by Turku PET Centre.

%description -l pl.UTF-8
PET Miscellaneous - biblioteka różnych funkcji Turku PET Centre.

%package devel
Summary:	Header files for libtpcmisc library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libtpcmisc
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libtpcmisc library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libtpcmisc.

%package static
Summary:	Static libtpcmisc library
Summary(pl.UTF-8):	Statyczna biblioteka libtpcmisc
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libtpcmisc library.

%description static -l pl.UTF-8
Statyczna biblioteka libtpcmisc.

%prep
%setup -q -c
rm -r trunk %{name}_*/autom4te.cache
mv %{name}_*/* .
rmdir %{name}_*
%patch0 -p1

%build
%{__make} libtpcmisc.la \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -std=gnu99 -Wall \$(INCLUDE) \$(ANSI)" \
	LDFLAGS="%{rpmldflags}" \
	PET_LIB=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}

%{__make} libinstall \
	DESTDIR=$RPM_BUILD_ROOT \
	PET_LIB=%{_libdir}

install -d $RPM_BUILD_ROOT%{_includedir}/tpc
install include/*.h $RPM_BUILD_ROOT%{_includedir}/tpc

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc History Readme
%attr(755,root,root) %{_libdir}/libtpcmisc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtpcmisc.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtpcmisc.so
%{_libdir}/libtpcmisc.la
%{_includedir}/tpc

%files static
%defattr(644,root,root,755)
%{_libdir}/libtpcmisc.a
