import React from 'react';
import clsx from 'clsx';
import TOCItems from '@theme/TOCItems';
import styles from './styles.module.css';
import { useState, useEffect } from 'react';

const LINK_CLASS_NAME = 'table-of-contents__link toc-highlight';
const LINK_ACTIVE_CLASS_NAME = 'table-of-contents__link--active';

export default function TOC({ className, ...props }) {
  const [tocIsHidden, setTocIsHidden] = useState(false);
  const [isHovering, setIsHovering] = useState(false);

  const handleMouseEnter = () => setIsHovering(true);
  const handleMouseLeave = () => setIsHovering(false);

  const divStyle = {
    transform: `translateX(${tocIsHidden ? '100%' : '0%'})`,
    opacity: `${isHovering ? '1' : tocIsHidden ? '0' : '0.4'}`,
    transition: 'transform 0.3s ease-in-out, opacity 0.1s ease-in-out',
  }

  useEffect(() => {
    const toggleSidebarNotionStyle = (event) => {
      if ((event.metaKey || event.ctrlKey) && event.key === 'b') {
        setTocIsHidden(tocIsHidden => !tocIsHidden)
      }
    };

    window.addEventListener('keydown', toggleSidebarNotionStyle);

    return () => {
      window.removeEventListener('keydown', toggleSidebarNotionStyle);
    };
  }, []);

  return (
    <div style={divStyle}
      onMouseEnter={handleMouseEnter}
      onMouseLeave={handleMouseLeave}
      className={clsx(styles.tableOfContents, 'thin-scrollbar', className)} >
      <TOCItems
        {...props}
        linkClassName={LINK_CLASS_NAME}
        linkActiveClassName={LINK_ACTIVE_CLASS_NAME}
      />
    </div >
  );
}
