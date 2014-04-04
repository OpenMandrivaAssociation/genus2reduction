Name:           genus2reduction
Version:        0.3
Release:        2
Summary:        Computes Reductions of Genus 2 Proper Smooth Curves
Group:          Sciences/Mathematics
License:        GPLv2
URL:            http://www.math.u-bordeaux1.fr/~qliu/G2R/
Source0:        http://www.math.u-bordeaux1.fr/~qliu/G2R/genus2reduction-%{version}.tar.gz
# License clarification:
Source1:        genus2reduction.mbox
# More license clarification:
Source2:        genus2reduction-licenseinfo.txt
# Adapt to pari 2.5
Patch0:         genus2reduction-compile.patch

BuildRequires:  libpari-devel

%description
Computes the conductor and reduction types for a genus 2 hyperelliptic
curve.

As an example of genus2reduction's functionality, let C be a proper
smooth curve of genus 2 defined by a hyperelliptic equation
y^2+Q(x)y=P(x), where P(x) and Q(x) are polynomials with rational
coefficients such that deg(Q(x))<4, deg(P(x))<7.  Let J(C) be the
Jacobian of C, let X be the minimal regular model of C over the ring of
integers Z.

This program determines the reduction of C at any prime number p (that
is the special fiber X_p of X over p), and the exponent f of the
conductor of J(C) at p.

%prep
%setup -q
%patch0
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .
find . -type f | xargs chmod a+r

%build
make CC="%{__cc}" CFLAGS="$RPM_OPT_FLAGS -I/usr/include/pari"

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -p -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%files
%doc README %{name}.mbox %{name}-licenseinfo.txt
%{_bindir}/%{name}
