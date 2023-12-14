import React from 'react';
import { translate } from '@docusaurus/Translate';
import CollapseButtonIcon from '@site/src/components/CollapseButtonIcon';
import styles from './styles.module.css';

export default function DocRootLayoutSidebarExpandButton({ toggleSidebar }) {
  return (
    <div
      className={styles.expandButton}
      title={translate({
        id: 'theme.docs.sidebar.expandButtonTitle',
        message: 'Expand sidebar',
        description:
          'The ARIA label and title attribute for expand button of doc sidebar',
      })}
      aria-label={translate({
        id: 'theme.docs.sidebar.expandButtonAriaLabel',
        message: 'Expand sidebar',
        description:
          'The ARIA label and title attribute for expand button of doc sidebar',
      })}
      tabIndex={0}
      role="button"
      onKeyDown={toggleSidebar}
      onClick={toggleSidebar}>
      <CollapseButtonIcon isReversed />
    </div>
  );
}
