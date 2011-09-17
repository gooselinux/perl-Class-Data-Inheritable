Name:           perl-Class-Data-Inheritable
Version:        0.08
Release:        3.1%{?dist}
Summary:        Inheritable, overridable class data
Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Class-Data-Inheritable/
Source0:        http://search.cpan.org/CPAN/authors/id/T/TM/TMTM/Class-Data-Inheritable-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl >= 1:5.6.1, perl(Test::More)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# For improved tests
BuildRequires: perl(Test::Pod::Coverage) >= 1.00
BuildRequires: perl(Test::Pod) >= 1.00

%description
Class::Data::Inheritable is for creating accessor/mutators to 
class data. That is, if you want to store something about your 
class as a whole (instead of about a single object). This data 
is then inherited by your subclasses and can be overriden.

%prep
%setup -q -n Class-Data-Inheritable-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{perl_vendorlib}/Class/
%{_mandir}/man3/*.3*


%changelog
* Mon Apr 26 2010 Dennis Gregorovic <dgregor@redhat.com> - 0.08-3.1
- Rebuilt for RHEL 6
Related: rhbz#566527

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul 09 2008 Ralf Corsépius <rc040203@freenet.de> - 0.08-1
- Upstream update.
- BR: perl(Test::Pod), perl(Test::Pod::Coverage).

* Wed Jul 09 2008 Ralf Corsépius <rc040203@freenet.de> - 0.06-5
- Fix broken Source0-URL.

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.06-4
- Rebuild for perl 5.10 (again)

* Mon Jan 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.06-3
- rebuild for new perl

* Fri Aug 24 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.06-2
- license fix

* Wed Jan 17 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.06-1
- bump to 0.06

* Thu Sep 14 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.05-1
- bump to 0.05

* Mon Jan  9 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.04-1
- bump to 0.04

* Sun Jul 10 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.02-3
- changed /Class/Data to /Class, for proper ownership

* Fri Jul  8 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.02-2
- cleanups

* Wed Jul  6 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.02-1
- Initial package for Fedora Extras
