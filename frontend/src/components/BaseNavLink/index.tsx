export const BaseNavLink = (props: {
  href: string;
  icon: string;
  label?: string;
}) => {
  return (
    <a className="base-nav-link" href={props.href}>
      {props.label && <span>{props.label}</span>}
      <i className={props.icon}></i>
    </a>
  );
};
