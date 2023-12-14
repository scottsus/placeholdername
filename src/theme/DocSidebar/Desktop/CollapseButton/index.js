import React from 'react';
import clsx from 'clsx';
import { translate } from '@docusaurus/Translate';
import CollapseButtonIcon from '@site/src/components/CollapseButtonIcon';
import styles from './styles.module.css';

export default function CollapseButton({ onClick }) {
  return (
    <button
      type="button"
      title={translate({
        id: 'theme.docs.sidebar.collapseButtonTitle',
        message: 'Collapse sidebar',
        description: 'The title attribute for collapse button of doc sidebar',
      })}
      aria-label={translate({
        id: 'theme.docs.sidebar.collapseButtonAriaLabel',
        message: 'Collapse sidebar',
        description: 'The title attribute for collapse button of doc sidebar',
      })}
      className={clsx(
        'button button--secondary button--outline',
        styles.collapseSidebarButton,
      )}
      onClick={onClick}>
      <CollapseButtonIcon />
    </button>
  );
}
