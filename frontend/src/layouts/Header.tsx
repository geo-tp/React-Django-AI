import { BaseNavLink } from "../components/BaseNavLink";
import { NavLogo } from "../components/NavLogo";

export const Header = () => {
  return (
    <header className="header">
      <NavLogo />
      <nav>
        <BaseNavLink
          href="https://github.com/geo-tp/React-Django-AI"
          icon="fab fa-github"
        />
      </nav>
    </header>
  );
};
