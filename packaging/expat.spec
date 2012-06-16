Name:           expat
Version:        2.1.0
Release:        1
Summary:        An XML parser library
Group:          System/Libraries
Source:         http://download.sourceforge.net/expat/expat-%{version}.tar.gz
Source1001:     expat.manifest 

License:        MIT
Url:            http://www.libexpat.org/

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

%prep
%setup -q
%build
cp %{SOURCE1001} .
%configure 
make %{?_smp_mflags}

%install
rm -f examples/*.dsp

%make_install

%remove_docs

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%manifest expat.manifest
%{_bindir}/*
/%{_libdir}/lib*.so.*

%files devel
%manifest expat.manifest
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*.h

