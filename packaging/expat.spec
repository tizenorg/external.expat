#sbs-git:slp/unmodified/expat expat 2.0.1-7 8603e1097e4ff351330178cc3719b35d845b5c5e
Name:           expat
Version:        2.0.1
Release:        8.1
Summary:        An XML parser library
Group:          System/Libraries
Source:         http://download.sourceforge.net/expat/expat-%{version}.tar.gz
Source1001: packaging/expat.manifest 
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
cp %{SOURCE1001} .
rm -rf autom4te*.cache
cp `aclocal --print-ac-dir`/libtool.m4 conftools || exit 1
libtoolize --copy --force --automake && aclocal && autoheader && autoconf
export CFLAGS="%{optflags} -fPIC"
%configure --libdir=/%{_lib}
make %{?_smp_mflags}

%install

rm -f examples/*.dsp
chmod 644 README COPYING Changes doc/* examples/*

%make_install

mkdir -p %{buildroot}%{_libdir}
mv %{buildroot}/%{_lib}/libexpat.so %{buildroot}%{_libdir}

lib=`echo %{buildroot}/%{_lib}/libexpat.so.*.*`
ln -sf ../../%{_lib}/`basename ${lib}` %{buildroot}%{_libdir}/libexpat.so

%check
make check

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

%files devel
%manifest expat.manifest
%defattr(-,root,root)
%{_libdir}/lib*.so
%{_includedir}/*.h

%files doc
%manifest expat.manifest
%defattr(-,root,root,-)
%doc %{_mandir}/*/*
%doc README
%doc Changes doc examples
%changelog
* Wed Dec 23 2009 Anas Nashif <anas.nashif@intel.com> - 2.0.1
- fixed some lint errors
- applied patch to be able to run make check
* Tue Dec 22 2009 Passion Zhao <passion.zhao@intel.com> - 2.0.1-8
- Disable the CVE-2009-3560 patch to fix the perl-XML-Parser build failure
  This upstream patch will be integrated after more validation.
* Wed Dec  9 2009 Passion Zhao <passion.zhao@intel.com> - 2.0.1-7
- add security fix for CVE-2009-3560: buffer over-read risk in big2_toUtf8()
* Fri Nov  6 2009 Passion Zhao <passion.zhao@intel.com> - 2.0.1-6
- add security fix for CVE-2009-3720
* Tue Dec  9 2008 Anas Nashif <anas.nashif@intel.com> 2.0.1
- do not install static libs
* Fri Dec  5 2008 Arjan van de Ven <arjan@linux.intel.com> 2.0.1
- Split out a -doc package
* Wed Jul 23 2008 Vivian Zhang <vivian.zhang@intel.com> 
- Add %%doc to man in %%files
* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.0.1-5
- Autorebuild for GCC 4.3
* Wed Jan 23 2008 Joe Orton <jorton@redhat.com> 2.0.1-4
- chmod 644 even more documentation (#429806)
* Tue Jan  8 2008 Joe Orton <jorton@redhat.com> 2.0.1-3
- chmod 644 the documentation (#427950)
* Wed Aug 22 2007 Joe Orton <jorton@redhat.com> 2.0.1-2
- rebuild
* Wed Aug  8 2007 Joe Orton <jorton@redhat.com> 2.0.1-1
- update to 2.0.1
- fix the License tag
- drop the .la file
* Sun Feb  4 2007 Joe Orton <jorton@redhat.com> 1.95.8-10
- remove trailing dot in Summary (#225742)
- use preferred BuildRoot per packaging guidelines (#225742)
* Tue Jan 30 2007 Joe Orton <jorton@redhat.com> 1.95.8-9
- regenerate configure/libtool correctly (#199361)
- strip DSP files from examples (#186889)
- fix expat.h compilation with g++ -pedantic (#190244)
* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.95.8-8.2.1
- rebuild
* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.95.8-8.2
- bump again for double-long bug on ppc(64)
* Tue Feb  7 2006 Jesse Keating <jkeating@redhat.com> - 1.95.8-8.1
- rebuilt for new gcc4.1 snapshot and glibc changes
* Tue Jan 31 2006 Joe Orton <jorton@redhat.com> 1.95.8-8
- restore .la file for apr-util
* Mon Jan 30 2006 Joe Orton <jorton@redhat.com> 1.95.8-7
- move library to /lib (#178743)
- omit .la file (#170031)
* Fri Dec  9 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt
* Tue Mar  8 2005 Joe Orton <jorton@redhat.com> 1.95.8-6
- rebuild
* Thu Nov 25 2004 Ivana Varekova <varekova@redhat.com> 1.95.8
- update to 1.95.8
* Wed Jun 16 2004 Jeff Johnson <jbj@jbj.org> 1.95.7-4
- add -fPIC (#125586).
* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt
* Fri Jun 11 2004 Jeff Johnson <jbj@jbj.org> 1.95.7-2
- fix: malloc failure from dbus test suite (#124747).
* Tue Mar  2 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt
* Sun Feb 22 2004 Joe Orton <jorton@redhat.com> 1.95.7-1
- update to 1.95.7, include COPYING file in main package
* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt
* Wed Sep 17 2003 Matt Wilson <msw@redhat.com> 1.95.5-6
- rebuild again for #91211
* Tue Sep 16 2003 Matt Wilson <msw@redhat.com> 1.95.5-5
- rebuild to fix gzip'ed file md5sums (#91211)
* Tue Jun 17 2003 Jeff Johnson <jbj@redhat.com> 1.95.5-4
- rebuilt because of crt breakage on ppc64.
* Wed Jun  4 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt
* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt
* Mon Nov 11 2002 Jeff Johnson <jbj@redhat.com> 1.95.5-1
- update to 1.95.5.
* Mon Aug 19 2002 Trond Eivind Glomsrød <teg@redhat.com> 1,95.4-1
- 1.95.4. 1.95.3 was withdrawn by the expat developers.
* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild
* Thu Jun  6 2002 Trond Eivind Glomsrød <teg@redhat.com> 1,95.3-1
- 1.95.3
* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild
* Fri Mar 22 2002 Trond Eivind Glomsrød <teg@redhat.com>
- Change a prereq in -devel on main package to a req
- License from MIT/X11 to BSD
* Wed Mar 13 2002 Trond Eivind Glomsrød <teg@redhat.com>
- 1.95.2
* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.
* Tue Oct 24 2000 Jeff Johnson <jbj@redhat.com>
- update to 1.95.1
* Sun Oct  8 2000 Jeff Johnson <jbj@redhat.com>
- Create.
