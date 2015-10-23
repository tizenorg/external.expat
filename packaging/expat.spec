Name:           expat
Version:        2.0.1
Release:        8
Summary:        An XML parser library
Group:          System/Libraries
Source:         %{name}-%{version}.tar.gz
Patch0:         expat-2.0.1-CVE-2009-3720.diff
Patch1:         expat-2.0.1-confcxx.patch

License:        MIT
Url:            http://www.libexpat.org/
BuildRequires:  autoconf,
BuildRequires:  automake,
BuildRequires:  libtool

%description
This is expat, the C library for parsing XML, written by James Clark. Expat
is a stream oriented XML parser. This means that you register handlers with
the parser prior to starting the parse. These handlers are called when the
parser discovers the associated structures in the document being parsed. A
start tag is an example of the kind of structures for which you may
register handlers.

%package devel
Summary:        Libraries and header files to develop applications using expat
Group:          Development/Libraries
Requires:       expat = %{version}

%description devel
The expat-devel package contains the libraries, include files and documentation
to develop XML applications with expat.

%package doc
Summary:        Documentation for the expat package
Group:          Development/Documentation
Requires:       expat = %{version}

%description doc
Documentation for the expat package

%prep
%setup -q
%patch0 -p0 -b .CVE-2009-3720
%patch1 -p1 -b .confcxx
%build
rm -rf autom4te*.cache
cp `aclocal --print-ac-dir`/libtool.m4 conftools || exit 1
libtoolize --copy --force --automake && aclocal && autoheader && autoconf
export CFLAGS="%{optflags} -fPIC"
%configure --libdir=/%{_lib}
make %{?_smp_mflags}

%install

mkdir -p %{buildroot}/usr/share/license
cp COPYING %{buildroot}/usr/share/license/%{name}

rm -f examples/*.dsp
chmod 644 README COPYING Changes doc/* examples/*

%make_install

mkdir -p %{buildroot}%{_libdir}
mv %{buildroot}/%{_lib}/libexpat.so %{buildroot}%{_libdir}

lib=`echo %{buildroot}/%{_lib}/libexpat.so.*.*`
ln -sf ../../%{_lib}/`basename ${lib}` %{buildroot}%{_libdir}/libexpat.so

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%manifest expat.manifest
%defattr(-,root,root,-)
%doc COPYING
%{_bindir}/*
/%{_lib}/lib*.so.*
/usr/share/license/%{name}

%files devel
%defattr(-,root,root)
%{_libdir}/lib*.so
%{_includedir}/*.h

%files doc
%defattr(-,root,root,-)
%doc %{_mandir}/*/*
%doc README
%doc Changes doc examples
